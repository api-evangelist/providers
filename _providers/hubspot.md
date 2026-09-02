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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 181
  human_in_the_loop: 3
  name: Hubspot Agentic Access
  operation_count: 260
  slug: hubspot-agentic-access
  summary_line: 260 operations · 181 acting · 3 human-in-the-loop
api_count: 25
apis:
- description: Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags.
  name: HubSpot Posts API
  slug: hubspot-posts-api
- description: 'URL redirects allow you to redirect traffic from a HubSpot-hosted page or blog post to any URL. You can also update URL redirects in bulk and use a flexible pattern redirect to dynamically update the '
  name: HubSpot URL Redirects API
  slug: hubspot-url-redirects-api
- description: Pipelines allow you to track records through defined stages in a process, such as sales deals or support tickets. The pipelines endpoints allow you to create, retrieve, update, and delete pipelines an
  name: HubSpot Pipelines API
  slug: hubspot-pipelines-api
- description: Products represent the goods or services you sell in HubSpot. The products endpoints allow you to manage a product library which can be used to quickly add products to deals, generate quotes, and repo
  name: HubSpot Products API
  slug: hubspot-products-api
- description: Line items are individual instances of products that are attached to a deal or quote. The line items endpoints allow you to create, retrieve, update, and delete line item records, enabling detailed pr
  name: HubSpot Line Items API
  slug: hubspot-line-items-api
- description: Quotes allow you to share pricing information with prospects and customers. The quotes endpoints allow you to create and manage quotes with associated line items, deals, and contacts, and support feat
  name: HubSpot Quotes API
  slug: hubspot-quotes-api
- description: The CRM properties endpoints allow you to manage custom properties and view default property details for any CRM object type. You can create, retrieve, update, and delete properties for contacts, comp
  name: HubSpot CRM Properties API
  slug: hubspot-crm-properties-api
- description: The owners endpoints are used to retrieve the list of available owners for a HubSpot account. HubSpot uses owners to assign CRM object records to specific users, and owner IDs are used when setting re
  name: HubSpot Owners API
  slug: hubspot-owners-api
- description: 'The imports endpoints allow you to import contact, company, deal, and other CRM object data into a HubSpot account in bulk using CSV or Excel files. You can map file columns to HubSpot properties and '
  name: HubSpot CRM Imports API
  slug: hubspot-crm-imports-api
- description: 'Custom objects allow you to define and create CRM object types that represent data unique to your business. The custom objects API allows you to define schemas, create records, manage properties, and '
  name: HubSpot Custom Objects API
  slug: hubspot-custom-objects-api
- description: Marketing events are CRM objects that enable you to track marketing activities such as webinars along with the contacts who registered and attended. The marketing events API supports creating and mana
  name: HubSpot Marketing Events API
  slug: hubspot-marketing-events-api
- description: The forms endpoints allow you to create and manage HubSpot forms used for capturing lead information. Supported form types include HubSpot native forms, captured external forms, flow forms, and blog c
  name: HubSpot Forms API
  slug: hubspot-forms-api
- description: The workflows API allows you to programmatically create, retrieve, update, and delete HubSpot automation workflows. You can manage workflow definitions and automate business processes across CRM objec
  name: HubSpot Workflows API
  slug: hubspot-workflows-api
- description: The webhooks API allows you to subscribe to events occurring in a HubSpot account, receiving real-time notifications when CRM objects or conversations are created, updated, or deleted. You can configu
  name: HubSpot Webhooks API
  slug: hubspot-webhooks-api
- description: The user provisioning API allows you to create and manage users in a HubSpot account along with their roles, permissions, and team assignments. You can add, retrieve, update, and remove users programm
  name: HubSpot Settings User Provisioning API
  slug: hubspot-settings-user-provisioning-api
- description: The blog tags API allows you to create, manage, and organize blog post tags in HubSpot CMS. Tags help organize blog content and improve discoverability. You can create, retrieve, update, and delete ta
  name: HubSpot Blog Tags API
  slug: hubspot-blog-tags-api
- description: 'The site search API allows you to search the content of HubSpot-hosted sites, including site pages, blog posts, landing pages, and knowledge articles. You can build custom site search experiences and '
  name: HubSpot CMS Site Search API
  slug: hubspot-cms-site-search-api
- description: The CMS content audit API allows you to query audit logs of CMS changes that occurred within your HubSpot account. You can filter and sort on content object changes by type, time period, or HubSpot us
  name: HubSpot CMS Content Audit API
  slug: hubspot-cms-content-audit-api
- description: The files API allows you to upload, manage, and organize files in HubSpot's file manager. You can upload files, organize them into folders, control file accessibility and privacy settings, retrieve fi
  name: HubSpot Files API
  slug: hubspot-files-api
- description: The feedback submissions API allows you to retrieve survey response data from HubSpot surveys including NPS, CSAT, CES, and custom surveys. This is a read-only API that provides access to existing sur
  name: HubSpot Feedback Submissions API
  slug: hubspot-feedback-submissions-api
- description: The leads API enables you to manage lead records in HubSpot. Leads are contacts or companies that are potential customers who have shown interest in your products or services. You can create, retrieve
  name: HubSpot Leads API
  slug: hubspot-leads-api
- description: The goals API enables you to sync user-specific sales and service team quotas between HubSpot and external systems. Goals are used to create user-specific quotas based on templates provided by HubSpot
  name: HubSpot Goals API
  slug: hubspot-goals-api
- description: The orders API enables you to create and manage ecommerce order data in HubSpot. You can create orders, manage associations to contacts, line items, payments, and invoices, and track fulfillment progr
  name: HubSpot Orders API
  slug: hubspot-orders-api
- description: The carts API enables you to create and manage ecommerce cart data in HubSpot. You can sync cart information between HubSpot and external ecommerce platforms, manage cart properties like pricing and c
  name: HubSpot Carts API
  slug: hubspot-carts-api
- description: The invoices API allows you to create, manage, retrieve, and delete invoices used for billing customers. Invoices progress through draft, open, paid, and voided statuses, and can be configured with di
  name: HubSpot Invoices API
  slug: hubspot-invoices-api
- description: The taxes API enables you to create and associate tax objects as part of the pricing details for quotes and invoices. Taxes are used in conjunction with discounts and fees when determining pricing tot
  name: HubSpot Taxes API
  slug: hubspot-taxes-api
- description: 'The fees API allows you to create and manage fees that can be included in invoices and legacy quotes. Fees support fixed dollar amounts or percentage-based values and are used alongside discounts and '
  name: HubSpot Fees API
  slug: hubspot-fees-api
- description: The discounts API enables you to create and associate discounts as part of the pricing details for quotes. Discounts work alongside fees and taxes in the quote pricing workflow, being applied first in
  name: HubSpot Discounts API
  slug: hubspot-discounts-api
- description: The communications API allows you to log WhatsApp, LinkedIn, or SMS messages to CRM record timelines. You can create, retrieve, update, and manage message engagement records and associate them with co
  name: HubSpot Engagement Communications API
  slug: hubspot-engagement-communications-api
- description: The postal mail engagement API allows you to log postal mail sent to or received from contacts or companies on their CRM records. You can create, retrieve, update, and delete postal mail engagement re
  name: HubSpot Engagement Postal Mail API
  slug: hubspot-engagement-postal-mail-api
- description: The transactional email API enables sending template-based transactional emails through HubSpot using the Single Send API and managing SMTP tokens. You can send emails for commerce receipts, account u
  name: HubSpot Transactional Email API
  slug: hubspot-transactional-email-api
- description: 'The subscription preferences API allows you to manage email subscription details for contacts in your account. You can retrieve subscription types, check contact preferences, subscribe or unsubscribe '
  name: HubSpot Subscription Preferences API
  slug: hubspot-subscription-preferences-api
- description: The timeline events API enables technology partners to send custom event data from external systems into HubSpot for display on CRM record activity timelines. You can create event templates, define cu
  name: HubSpot Timeline Events API
  slug: hubspot-timeline-events-api
- description: 'The calling extensions SDK enables apps to provide a custom calling option to HubSpot users directly from CRM records. The SDK facilitates bidirectional communication between calling applications and '
  name: HubSpot Calling Extensions API
  slug: hubspot-calling-extensions-api
- description: The video conferencing API enables you to integrate custom video conferencing solutions into HubSpot's meeting creation workflow. You can configure webhook notifications for meeting creation, updates,
  name: HubSpot Video Conferencing API
  slug: hubspot-video-conferencing-api
- description: The account information API provides account configuration and usage data for HubSpot accounts. You can retrieve account details including portal ID, time zone, currency settings, and data center loca
  name: HubSpot Account Information API
  slug: hubspot-account-information-api
- description: 'The business units (brands) API provides information about brands tied to a HubSpot user. You can retrieve brand data including brand name, ID, and logo metadata for brands associated with a specific '
  name: HubSpot Business Units API
  slug: hubspot-business-units-api
- description: The currencies API allows you to manage the currencies used in your HubSpot account. You can set your account's company currency, create additional currencies, update exchange rates, and configure aut
  name: HubSpot Currencies API
  slug: hubspot-currencies-api
- description: Operations for retrieving and validating OAuth access token metadata
  name: HubSpot Access Tokens API
  slug: hubspot-access-tokens-api
- description: Operations to create and manage custom workflow action definitions
  name: HubSpot Action Definitions API
  slug: hubspot-action-definitions-api
- description: Operations to manage serverless functions associated with action definitions
  name: HubSpot Action Functions API
  slug: hubspot-action-functions-api
- description: Operations for managing conversation participants including visitors and agents.
  name: HubSpot Actors API
  slug: hubspot-actors-api
- description: Manage feature flag configurations at the application level
  name: HubSpot Application Feature Flags API
  slug: hubspot-application-feature-flags-api
- description: Create, update, and delete custom labels for association types
  name: HubSpot Association Label Management API
  slug: hubspot-association-label-management-api
- description: Retrieve and manage association type definitions across object types
  name: HubSpot Association Type Definitions API
  slug: hubspot-association-type-definitions-api
- description: Operations for managing subscription associations
  name: HubSpot Associations API
  slug: hubspot-associations-api
- description: Create, read, update, and delete individual call records
  name: HubSpot Basic Operations API
  slug: hubspot-basic-operations-api
- description: Batch operations for subscriptions
  name: HubSpot Batch API
  slug: hubspot-batch-api
- description: Perform bulk create, read, and archive operations on multiple associations
  name: HubSpot Batch Association Operations API
  slug: hubspot-batch-association-operations-api
- description: Perform bulk operations on multiple blog authors simultaneously
  name: HubSpot Batch Operations API
  slug: hubspot-batch-operations-api
- description: Perform bulk operations on portal flag states
  name: HubSpot Batch Portal Operations API
  slug: hubspot-batch-portal-operations-api
- description: Create, read, update, and delete individual blog author profiles
  name: HubSpot Blog Authors API
  slug: hubspot-blog-authors-api
- description: Operations for managing communication channels such as email, chat, and social media.
  name: HubSpot Channels API
  slug: hubspot-channels-api
- description: Operations for managing company records
  name: HubSpot Companies API
  slug: hubspot-companies-api
- description: Operations for managing contact records
  name: HubSpot Contacts API
  slug: hubspot-contacts-api
- description: Operations for managing deal records
  name: HubSpot Deals API
  slug: hubspot-deals-api
- description: Operations to view revision history of action definitions
  name: HubSpot Definition Revisions API
  slug: hubspot-definition-revisions-api
- description: Operations for managing and retrieving domain information
  name: HubSpot Domain Management API
  slug: hubspot-domain-management-api
- description: Manage blog post drafts and revision history
  name: HubSpot Drafts and Revisions API
  slug: hubspot-drafts-and-revisions-api
- description: Operations for managing email engagement records
  name: HubSpot Emails API
  slug: hubspot-emails-api
- description: Retrieve and query event completion data from CRM objects
  name: HubSpot Event Instances API
  slug: hubspot-event-instances-api
- description: Discover and retrieve available event type definitions
  name: HubSpot Event Types API
  slug: hubspot-event-types-api
- description: Operations for downloading, creating, updating, and deleting source code files
  name: HubSpot File Content API
  slug: hubspot-file-content-api
- description: Operations for extracting zip archives in the developer file system
  name: HubSpot File Extraction API
  slug: hubspot-file-extraction-api
- description: Operations for retrieving file and folder metadata
  name: HubSpot File Metadata API
  slug: hubspot-file-metadata-api
- description: Operations for validating source code files
  name: HubSpot File Validation API
  slug: hubspot-file-validation-api
- description: GDPR-compliant data management operations
  name: HubSpot GDPR Compliance API
  slug: hubspot-gdpr-compliance-api
- description: Operations for managing conversation inboxes where messages are organized and routed.
  name: HubSpot Inboxes API
  slug: hubspot-inboxes-api
- description: Operations for managing landing pages
  name: HubSpot Landing Pages API
  slug: hubspot-landing-pages-api
- description: Operations for managing CRM lists
  name: HubSpot Lists API
  slug: hubspot-lists-api
- description: Operations for managing meeting engagement records
  name: HubSpot Meetings API
  slug: hubspot-meetings-api
- description: Operations for managing list memberships
  name: HubSpot Memberships API
  slug: hubspot-memberships-api
- description: Operations for sending, receiving, and managing messages within conversation threads.
  name: HubSpot Messages API
  slug: hubspot-messages-api
- description: Manage multi-language author groups and language variations
  name: HubSpot Multi-Language Management API
  slug: hubspot-multi-language-management-api
- description: Create, retrieve, and delete associations between individual CRM objects
  name: HubSpot Object Associations API
  slug: hubspot-object-associations-api
- description: Advanced search operations for finding and filtering commerce payments
  name: HubSpot Payment Search API
  slug: hubspot-payment-search-api
- description: Manage feature flag states for specific portals (HubSpot accounts)
  name: HubSpot Portal Flag States API
  slug: hubspot-portal-flag-states-api
- description: Clone and duplicate existing blog posts
  name: HubSpot Post Cloning API
  slug: hubspot-post-cloning-api
- description: Schedule publication and manage post visibility
  name: HubSpot Publishing and Scheduling API
  slug: hubspot-publishing-and-scheduling-api
- description: Operations for managing OAuth refresh tokens
  name: HubSpot Refresh Tokens API
  slug: hubspot-refresh-tokens-api
- description: Operations for managing HubDB table rows
  name: HubSpot Rows API
  slug: hubspot-rows-api
- description: Operations for searching CRM objects
  name: HubSpot Search API
  slug: hubspot-search-api
- description: CRUD operations for individual commerce payment records
  name: HubSpot Single Payment Operations API
  slug: hubspot-single-payment-operations-api
- description: Send individual transactional emails using templates
  name: HubSpot Single Send API
  slug: hubspot-single-send-api
- description: Operations for managing site pages
  name: HubSpot Site Pages API
  slug: hubspot-site-pages-api
- description: Create, query, and manage SMTP API tokens for transactional email sending
  name: HubSpot SMTP Token Management API
  slug: hubspot-smtp-token-management-api
- description: Operations for managing subscription records
  name: HubSpot Subscriptions API
  slug: hubspot-subscriptions-api
- description: Operations for managing HubDB tables
  name: HubSpot Tables API
  slug: hubspot-tables-api
- description: Operations for managing task engagement records
  name: HubSpot Tasks API
  slug: hubspot-tasks-api
- description: Operations for creating, retrieving, updating, and archiving conversation threads.
  name: HubSpot Threads API
  slug: hubspot-threads-api
- description: Operations for managing ticket records
  name: HubSpot Tickets API
  slug: hubspot-tickets-api
- description: Operations for creating, refreshing, and managing OAuth tokens
  name: HubSpot Token Management API
  slug: hubspot-token-management-api
- description: Operations to complete workflow action callbacks for asynchronous actions
  name: HubSpot Workflow Callbacks API
  slug: hubspot-workflow-callbacks-api
arazzos:
- description: Create a note engagement and associate it to a CRM record.
  name: HubSpot Add a Note to a Record
  slug: hubspot-add-note-to-record-workflow
- description: Find a deal by name and move it to a new pipeline stage.
  name: HubSpot Advance a Deal Stage
  slug: hubspot-advance-deal-stage-workflow
- description: Create an association between two CRM objects, then list it back to verify.
  name: HubSpot Associate Two CRM Records
  slug: hubspot-associate-records-workflow
- description: Batch-create a set of contacts then batch-read them back to verify.
  name: HubSpot Batch Import Contacts
  slug: hubspot-batch-import-contacts-workflow
- description: Discover available analytics event types, then query event instances for a CRM object.
  name: HubSpot Query Behavioral Analytics Events
  slug: hubspot-capture-analytics-event-workflow
- description: Create a CMS site page in draft, then publish its draft live.
  name: HubSpot Create and Publish a CMS Page
  slug: hubspot-create-cms-page-workflow
- description: Create a contact, create a company, and associate the two records.
  name: HubSpot Create a Contact With a Company
  slug: hubspot-create-contact-with-company-workflow
- description: Create a deal and associate it to an existing contact and company.
  name: HubSpot Create a Deal With Associations
  slug: hubspot-create-deal-with-associations-workflow
- description: Create a task engagement with a due date and associate it to a record.
  name: HubSpot Create a Follow-up Task
  slug: hubspot-create-followup-task-workflow
- description: Find a contact by email, create a support ticket, and associate them.
  name: HubSpot Create a Ticket For a Contact
  slug: hubspot-create-ticket-for-contact-workflow
- description: List commerce payments, then retrieve the full record for the first payment.
  name: HubSpot List and Read Commerce Payments
  slug: hubspot-list-payments-workflow
- description: Create a call engagement and associate it to a contact in a single flow.
  name: HubSpot Log a Call on a Contact
  slug: hubspot-log-call-on-contact-workflow
- description: Create an email engagement and associate it to a contact.
  name: HubSpot Log an Email Engagement
  slug: hubspot-log-email-engagement-workflow
- description: Create a meeting engagement and associate it to a deal.
  name: HubSpot Log a Meeting on a Deal
  slug: hubspot-log-meeting-on-deal-workflow
- description: Create a HubDB table, add a row to its draft, then publish the table.
  name: HubSpot Manage a HubDB Table
  slug: hubspot-manage-hubdb-table-workflow
- description: Retrieve a commerce subscription, then update its properties or archive it.
  name: HubSpot Manage a Commerce Subscription
  slug: hubspot-manage-subscription-workflow
- description: Exchange an authorization code for tokens, refresh the access token, then read its metadata.
  name: HubSpot OAuth Token Lifecycle
  slug: hubspot-oauth-token-lifecycle-workflow
- description: Resolve or create a blog author, create a blog post, then publish or schedule it.
  name: HubSpot Publish a Blog Post
  slug: hubspot-publish-blog-post-workflow
- description: List conversation threads, retrieve one, then send a reply message.
  name: HubSpot Respond to a Conversation
  slug: hubspot-respond-to-conversation-workflow
- description: Search CRM objects with a filter, then add the matches to a static list.
  name: HubSpot Search and Add to a List
  slug: hubspot-search-and-add-to-list-workflow
- description: Create an SMTP token for a campaign, read it back, then send a transactional email.
  name: HubSpot Send a Transactional Marketing Email
  slug: hubspot-send-marketing-email-workflow
- description: List tasks then update a task's status and priority.
  name: HubSpot Triage Tasks
  slug: hubspot-triage-tasks-workflow
- description: Find a contact by email and update it if it exists, otherwise create it.
  name: HubSpot Upsert a Contact
  slug: hubspot-upsert-contact-workflow
artifact_total: 2545
asyncapis:
- description: 'The HubSpot Webhooks API enables real-time event notifications for changes to CRM objects and conversations in a HubSpot portal. When subscribed events occur, HubSpot delivers HTTP POST requests to a '
  name: HubSpot Webhooks API
  slug: hubspot-webhooks-asyncapi
collections:
- collection_type: postman
  name: HubSpot Analytics Events API
  slug: postman-hubspot-analytics-events-api
- collection_type: postman
  name: HubSpot Blog Authors API
  slug: postman-hubspot-authors-api
- collection_type: postman
  name: HubSpot Blog Posts API
  slug: postman-hubspot-blog-posts-api
- collection_type: postman
  name: HubSpot CMS HubDB API
  slug: postman-hubspot-cms-hubdb-api
- collection_type: postman
  name: HubSpot CMS Pages API
  slug: postman-hubspot-cms-pages-api
- collection_type: postman
  name: HubSpot Commerce Payments API
  slug: postman-hubspot-commerce-payments-api
- collection_type: postman
  name: HubSpot Commerce Subscriptions API
  slug: postman-hubspot-commerce-subscriptions-api
- collection_type: postman
  name: HubSpot Conversations API
  slug: postman-hubspot-conversations-api
- collection_type: postman
  name: HubSpot CRM Associations API
  slug: postman-hubspot-crm-associations-api
- collection_type: postman
  name: HubSpot CRM Companies API
  slug: postman-hubspot-crm-companies-api
- collection_type: postman
  name: HubSpot CRM Contacts API
  slug: postman-hubspot-crm-contacts-api
- collection_type: postman
  name: HubSpot CRM Deals API
  slug: postman-hubspot-crm-deals-api
- collection_type: postman
  name: HubSpot CRM Feature Flags API
  slug: postman-hubspot-crm-feature-flags-api
- collection_type: postman
  name: HubSpot CRM Lists API
  slug: postman-hubspot-crm-lists-api
- collection_type: postman
  name: HubSpot CRM Search API
  slug: postman-hubspot-crm-search-api
- collection_type: postman
  name: HubSpot CRM Tickets API
  slug: postman-hubspot-crm-tickets-api
- collection_type: postman
  name: HubSpot Custom Workflow Actions API
  slug: postman-hubspot-custom-workflow-actions-api
- collection_type: postman
  name: HubSpot CMS Domains API
  slug: postman-hubspot-domains-api
- collection_type: postman
  name: HubSpot CRM Engagement Calls API
  slug: postman-hubspot-engagement-calls-api
- collection_type: postman
  name: HubSpot Engagement Emails API
  slug: postman-hubspot-engagement-emails-api
- collection_type: postman
  name: HubSpot Engagement Meetings API
  slug: postman-hubspot-engagement-meetings-api
- collection_type: postman
  name: HubSpot CRM Engagement Notes API
  slug: postman-hubspot-engagement-notes
- collection_type: postman
  name: HubSpot Engagement Tasks API
  slug: postman-hubspot-engagement-tasks-api
- collection_type: postman
  name: HubSpot Marketing Transactional Email API
  slug: postman-hubspot-marketing-emal-api
- collection_type: postman
  name: HubSpot OAuth API
  slug: postman-hubspot-oauth-api
- collection_type: postman
  name: HubSpot CMS Source Code API
  slug: postman-hubspot-source-code-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HubSpot Analytics Events Access Tokens API
  slug: open-hubspot-access-tokens-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Action Definitions API
  slug: open-hubspot-action-definitions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Action Functions API
  slug: open-hubspot-action-functions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Actors API
  slug: open-hubspot-actors-api
- collection_type: open
  name: HubSpot Analytics Events API
  slug: open-hubspot-analytics-events-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Application Feature Flags API
  slug: open-hubspot-application-feature-flags-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Association Label Management API
  slug: open-hubspot-association-label-management-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Association Type Definitions API
  slug: open-hubspot-association-type-definitions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Associations API
  slug: open-hubspot-associations-api
- collection_type: open
  name: HubSpot Blog Authors API
  slug: open-hubspot-authors-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Basic Operations API
  slug: open-hubspot-basic-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch API
  slug: open-hubspot-batch-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch Association Operations API
  slug: open-hubspot-batch-association-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch Operations API
  slug: open-hubspot-batch-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch Portal Operations API
  slug: open-hubspot-batch-portal-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Blog Authors API
  slug: open-hubspot-blog-authors-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Blog Posts API
  slug: open-hubspot-blog-posts-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Channels API
  slug: open-hubspot-channels-api
- collection_type: open
  name: HubSpot CMS HubDB API
  slug: open-hubspot-cms-hubdb-api
- collection_type: open
  name: HubSpot CMS Pages API
  slug: open-hubspot-cms-pages-api
- collection_type: open
  name: HubSpot Commerce Payments API
  slug: open-hubspot-commerce-payments-api
- collection_type: open
  name: HubSpot Commerce Subscriptions API
  slug: open-hubspot-commerce-subscriptions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Companies API
  slug: open-hubspot-companies-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Contacts API
  slug: open-hubspot-contacts-api
- collection_type: open
  name: HubSpot Conversations API
  slug: open-hubspot-conversations-api
- collection_type: open
  name: HubSpot CRM Associations API
  slug: open-hubspot-crm-associations-api
- collection_type: open
  name: HubSpot CRM Companies API
  slug: open-hubspot-crm-companies-api
- collection_type: open
  name: HubSpot CRM Contacts API
  slug: open-hubspot-crm-contacts-api
- collection_type: open
  name: HubSpot CRM Deals API
  slug: open-hubspot-crm-deals-api
- collection_type: open
  name: HubSpot CRM Feature Flags API
  slug: open-hubspot-crm-feature-flags-api
- collection_type: open
  name: HubSpot CRM Lists API
  slug: open-hubspot-crm-lists-api
- collection_type: open
  name: HubSpot CRM Search API
  slug: open-hubspot-crm-search-api
- collection_type: open
  name: HubSpot CRM Tickets API
  slug: open-hubspot-crm-tickets-api
- collection_type: open
  name: HubSpot Custom Workflow Actions API
  slug: open-hubspot-custom-workflow-actions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Deals API
  slug: open-hubspot-deals-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Definition Revisions API
  slug: open-hubspot-definition-revisions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Domain Management API
  slug: open-hubspot-domain-management-api
- collection_type: open
  name: HubSpot CMS Domains API
  slug: open-hubspot-domains-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Drafts and Revisions API
  slug: open-hubspot-drafts-and-revisions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Emails API
  slug: open-hubspot-emails-api
- collection_type: open
  name: HubSpot CRM Engagement Calls API
  slug: open-hubspot-engagement-calls-api
- collection_type: open
  name: HubSpot Engagement Emails API
  slug: open-hubspot-engagement-emails-api
- collection_type: open
  name: HubSpot Engagement Meetings API
  slug: open-hubspot-engagement-meetings-api
- collection_type: open
  name: HubSpot CRM Engagement Notes API
  slug: open-hubspot-engagement-notes
- collection_type: open
  name: HubSpot Engagement Tasks API
  slug: open-hubspot-engagement-tasks-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Event Instances API
  slug: open-hubspot-event-instances-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Event Types API
  slug: open-hubspot-event-types-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Content API
  slug: open-hubspot-file-content-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Extraction API
  slug: open-hubspot-file-extraction-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Metadata API
  slug: open-hubspot-file-metadata-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Validation API
  slug: open-hubspot-file-validation-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens GDPR Compliance API
  slug: open-hubspot-gdpr-compliance-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Inboxes API
  slug: open-hubspot-inboxes-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Landing Pages API
  slug: open-hubspot-landing-pages-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Lists API
  slug: open-hubspot-lists-api
- collection_type: open
  name: HubSpot Marketing Transactional Email API
  slug: open-hubspot-marketing-emal-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Meetings API
  slug: open-hubspot-meetings-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Memberships API
  slug: open-hubspot-memberships-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Messages API
  slug: open-hubspot-messages-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Multi-Language Management API
  slug: open-hubspot-multi-language-management-api
- collection_type: open
  name: HubSpot OAuth API
  slug: open-hubspot-oauth-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Object Associations API
  slug: open-hubspot-object-associations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Payment Search API
  slug: open-hubspot-payment-search-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Portal Flag States API
  slug: open-hubspot-portal-flag-states-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Post Cloning API
  slug: open-hubspot-post-cloning-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Publishing and Scheduling API
  slug: open-hubspot-publishing-and-scheduling-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Refresh Tokens API
  slug: open-hubspot-refresh-tokens-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Rows API
  slug: open-hubspot-rows-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Search API
  slug: open-hubspot-search-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Single Payment Operations API
  slug: open-hubspot-single-payment-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Single Send API
  slug: open-hubspot-single-send-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Site Pages API
  slug: open-hubspot-site-pages-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens SMTP Token Management API
  slug: open-hubspot-smtp-token-management-api
- collection_type: open
  name: HubSpot CMS Source Code API
  slug: open-hubspot-source-code-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Subscriptions API
  slug: open-hubspot-subscriptions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Tables API
  slug: open-hubspot-tables-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Tasks API
  slug: open-hubspot-tasks-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Threads API
  slug: open-hubspot-threads-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Tickets API
  slug: open-hubspot-tickets-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Token Management API
  slug: open-hubspot-token-management-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Workflow Callbacks API
  slug: open-hubspot-workflow-callbacks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hubspot-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/HubSpot/mcp-server/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hubspot-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hubspot-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hubspot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hubspot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hubspot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hubspot-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hubspot/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-add-note-to-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-advance-deal-stage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-associate-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-batch-import-contacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-capture-analytics-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-cms-page-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-contact-with-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-deal-with-associations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-followup-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-ticket-for-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-list-payments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-log-call-on-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-log-email-engagement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-log-meeting-on-deal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-manage-hubdb-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-manage-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-oauth-token-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-publish-blog-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-respond-to-conversation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-search-and-add-to-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-send-marketing-email-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-triage-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hubspot-upsert-contact-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hubspot
- group: docs
  title: ''
  type: APIReference
  url: https://api.hubspot.com/api-catalog-public/v1/apis
- group: start
  title: ''
  type: Portal
  url: https://developers.hubspot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/api/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.hubspot.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers
- group: operate
  title: ''
  type: Support
  url: https://developers.hubspot.com/slack
- group: company
  title: ''
  type: Blog
  url: https://developers.hubspot.com/blog
- group: company
  title: ''
  type: Newsletter
  url: https://offers.hubspot.com/developer-newsletter-signup
- group: other
  title: ''
  type: Events
  url: https://www.hubspot.com/developer-community-events
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.hubspot.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.hubspot.com/terms-of-service
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hubspot.com/docs/getting-started/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/guides/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/reference/api/overview
- group: start
  title: ''
  type: Login
  url: https://app.hubspot.com/login
- group: operate
  title: ''
  type: Contact
  url: https://offers.hubspot.com/crm-platform-demo
- group: docs
  title: ''
  type: Documentation
  url: https://www.hubspot.com/our-story
- group: company
  title: ''
  type: Blog
  url: https://blog.hubspot.com/
- group: auth
  title: ''
  type: Security
  url: https://legal.hubspot.com/security
- group: company
  title: ''
  type: Partners
  url: https://www.hubspot.com/partners/affiliates
- group: company
  title: ''
  type: Partners
  url: https://www.hubspot.com/partners
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hubspot.com/pricing/marketing/enterprise
- group: other
  title: ''
  type: Showcase
  url: https://www.hubspot.com/case-studies
- group: start
  title: ''
  type: Signup
  url: https://app.hubspot.com/signup/developers
- group: auth
  title: ''
  type: Authentication
  url: https://developers.hubspot.com/docs/api/intro-to-auth
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hubspot.com
- group: operate
  title: ''
  type: Support
  url: https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HubSpot
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/HubSpot/HubSpot-public-api-spec-collection
- group: build
  title: ''
  type: SDKs
  url: https://developers.hubspot.com/docs/api/client-libraries
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/hubspot
- group: other
  title: ''
  type: Resources
  url: https://www.postman.com/hubspot/hubspot-public-api-workspace/overview
- group: other
  title: ''
  type: Resources
  url: https://developers.hubspot.com/developer-tools
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hubspot.com/apisbytier
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hubspot-crm-object-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hubspot-crm-search-request-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-context.jsonld
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/hubspot-api-client/
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/@hubspot/api-client
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://rubygems.org/gems/hubspot-api-client
- group: build
  title: PHP SDK
  type: SDKs
  url: https://packagist.org/packages/hubspot/api-client
- group: build
  title: HubSpot CLI
  type: CLI
  url: https://www.npmjs.com/package/@hubspot/cli
- group: build
  title: HubSpot MCP Server
  type: GitHubRepository
  url: https://github.com/HubSpot/mcp-server
- group: build
  title: Calling Extensions SDK
  type: SDKs
  url: https://github.com/HubSpot/calling-extensions-sdk
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-analytics-events-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-authors-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-blog-posts-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-hubdb-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-pages-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-payments-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-subscriptions-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-conversations-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-associations-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-companies-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-contacts-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-deals-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-feature-flags-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-lists-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-search-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-tickets-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-custom-workflow-actions-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-domains-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-calls-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-emails-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-meetings-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-association-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-batch-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-filter-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-gdpr-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-next-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-note-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-paging-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-property-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-sort-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-tasks-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-marketing-emal-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-oauth-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hubspot-source-code-api-context.jsonld
- group: docs
  title: Spectral Rules
  type: Documentation
  url: rules/hubspot-spectral-rules.yml
- group: docs
  title: Vocabulary
  type: Documentation
  url: vocabulary/hubspot-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hubspot-mcp.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/HubSpot/noc-skills
- group: build
  title: ''
  type: Packages
  url: packages/hubspot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hubspot-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hubspot-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hubspot-security.txt
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/hubspot
- group: auth
  title: ''
  type: Compliance
  url: https://trust.hubspot.com/
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hubspot-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hubspot-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hubspot-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hubspot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hubspot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hubspot.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.hubspot.com/changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/hubspot-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hubspot-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/hubspot-cli.yml
- group: design
  title: ''
  type: Components
  url: components/hubspot-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hubspot-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hubspot-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/hubspot-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hubspot-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hubspot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hubspot-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hubspot.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.hubspot.com/signup/developers
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hubspot/hubspot-public-api-workspace/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hubspot.com/docs/reference/api/other-resources/error-handling
created: 2023/11/14
description: HubSpot is an AI-native customer platform built around the Smart CRM, unifying marketing, sales, customer service, content, commerce and operations on a single shared customer record. Its developer platform exposes that record through a broad REST surface at api.hubapi.com covering CRM objects and associations, engagements, lists and segments, marketing and transactional email, CMS pages, blogs and HubDB, conversations, commerce payments and subscriptions, custom workflow actions, webhooks and analytics events. HubSpot ships first-party Node, Python, Ruby and PHP clients, a CLI, OAuth 2.0 with a granular scope model, a public developer changelog, date-based API versioning and a hosted MCP server for agents.
examples:
- key_count: 2
  name: Analytics Events Api Event Instance Collection Example
  slug: analytics-events-api-event-instance-collection-example
- key_count: 6
  name: Analytics Events Api Event Instance Example
  slug: analytics-events-api-event-instance-example
- key_count: 1
  name: Analytics Events Api Event Type Collection Example
  slug: analytics-events-api-event-type-collection-example
- key_count: 2
  name: Analytics Events Api Paging Example
  slug: analytics-events-api-paging-example
- key_count: 2
  name: Analytics Events Api Paging Next Example
  slug: analytics-events-api-paging-next-example
- key_count: 2
  name: Analytics Events Api Paging Previous Example
  slug: analytics-events-api-paging-previous-example
- key_count: 4
  name: Authors Api Attach To Language Group Request Example
  slug: authors-api-attach-to-language-group-request-example
- key_count: 1
  name: Authors Api Batch Archive Input Example
  slug: authors-api-batch-archive-input-example
- key_count: 1
  name: Authors Api Batch Create Input Example
  slug: authors-api-batch-create-input-example
- key_count: 1
  name: Authors Api Batch Input Example
  slug: authors-api-batch-input-example
- key_count: 2
  name: Authors Api Batch Input Item Example
  slug: authors-api-batch-input-item-example
- key_count: 1
  name: Authors Api Batch Read Input Example
  slug: authors-api-batch-read-input-example
- key_count: 6
  name: Authors Api Batch Response Example
  slug: authors-api-batch-response-example
- key_count: 3
  name: Authors Api Blog Author Collection Example
  slug: authors-api-blog-author-collection-example
- key_count: 15
  name: Authors Api Blog Author Example
  slug: authors-api-blog-author-example
- key_count: 9
  name: Authors Api Blog Author Input Example
  slug: authors-api-blog-author-input-example
- key_count: 2
  name: Authors Api Create Language Variation Request Example
  slug: authors-api-create-language-variation-request-example
- key_count: 1
  name: Authors Api Detach From Language Group Request Example
  slug: authors-api-detach-from-language-group-request-example
- key_count: 1
  name: Authors Api Paging Example
  slug: authors-api-paging-example
- key_count: 2
  name: Authors Api Paging Next Example
  slug: authors-api-paging-next-example
- key_count: 1
  name: Authors Api Set Language Primary Request Example
  slug: authors-api-set-language-primary-request-example
- key_count: 4
  name: Blog Posts Api Attach To Language Group Request Example
  slug: blog-posts-api-attach-to-language-group-request-example
- key_count: 1
  name: Blog Posts Api Batch Input Example
  slug: blog-posts-api-batch-input-example
- key_count: 1
  name: Blog Posts Api Batch Input Item Example
  slug: blog-posts-api-batch-input-item-example
- key_count: 6
  name: Blog Posts Api Batch Response Example
  slug: blog-posts-api-batch-response-example
- key_count: 3
  name: Blog Posts Api Blog Post Collection Example
  slug: blog-posts-api-blog-post-collection-example
- key_count: 32
  name: Blog Posts Api Blog Post Example
  slug: blog-posts-api-blog-post-example
- key_count: 15
  name: Blog Posts Api Blog Post Input Example
  slug: blog-posts-api-blog-post-input-example
- key_count: 1
  name: Blog Posts Api Clone Request Example
  slug: blog-posts-api-clone-request-example
- key_count: 2
  name: Blog Posts Api Create Language Variation Request Example
  slug: blog-posts-api-create-language-variation-request-example
- key_count: 1
  name: Blog Posts Api Detach From Language Group Request Example
  slug: blog-posts-api-detach-from-language-group-request-example
- key_count: 2
  name: Blog Posts Api Paging Example
  slug: blog-posts-api-paging-example
- key_count: 2
  name: Blog Posts Api Paging Next Example
  slug: blog-posts-api-paging-next-example
- key_count: 2
  name: Blog Posts Api Paging Previous Example
  slug: blog-posts-api-paging-previous-example
- key_count: 1
  name: Blog Posts Api Push Live Request Example
  slug: blog-posts-api-push-live-request-example
- key_count: 1
  name: Blog Posts Api Reset Draft Request Example
  slug: blog-posts-api-reset-draft-request-example
- key_count: 2
  name: Blog Posts Api Restore Previous Version Request Example
  slug: blog-posts-api-restore-previous-version-request-example
- key_count: 2
  name: Blog Posts Api Schedule Request Example
  slug: blog-posts-api-schedule-request-example
- key_count: 1
  name: Blog Posts Api Set Language Primary Request Example
  slug: blog-posts-api-set-language-primary-request-example
- key_count: 4
  name: Blog Posts Api Version History Example
  slug: blog-posts-api-version-history-example
- key_count: 2
  name: Cms Hubdb Api Collection Response Hub Dbrow Example
  slug: cms-hubdb-api-collection-response-hub-dbrow-example
- key_count: 2
  name: Cms Hubdb Api Collection Response Hub Dbtable Example
  slug: cms-hubdb-api-collection-response-hub-dbtable-example
- key_count: 5
  name: Cms Hubdb Api Hub Dbcolumn Example
  slug: cms-hubdb-api-hub-dbcolumn-example
- key_count: 1
  name: Cms Hubdb Api Hub Dbrow Create Request Example
  slug: cms-hubdb-api-hub-dbrow-create-request-example
- key_count: 4
  name: Cms Hubdb Api Hub Dbrow Example
  slug: cms-hubdb-api-hub-dbrow-example
- key_count: 3
  name: Cms Hubdb Api Hub Dbtable Create Request Example
  slug: cms-hubdb-api-hub-dbtable-create-request-example
- key_count: 9
  name: Cms Hubdb Api Hub Dbtable Example
  slug: cms-hubdb-api-hub-dbtable-example
- key_count: 1
  name: Cms Hubdb Api Paging Example
  slug: cms-hubdb-api-paging-example
- key_count: 2
  name: Cms Pages Api Collection Response Page Example
  slug: cms-pages-api-collection-response-page-example
- key_count: 8
  name: Cms Pages Api Page Create Request Example
  slug: cms-pages-api-page-create-request-example
- key_count: 16
  name: Cms Pages Api Page Example
  slug: cms-pages-api-page-example
- key_count: 5
  name: Cms Pages Api Page Update Request Example
  slug: cms-pages-api-page-update-request-example
- key_count: 1
  name: Cms Pages Api Paging Example
  slug: cms-pages-api-paging-example
- key_count: 2
  name: Commerce Payments Api Association Input Example
  slug: commerce-payments-api-association-input-example
- key_count: 2
  name: Commerce Payments Api Association Result Example
  slug: commerce-payments-api-association-result-example
- key_count: 2
  name: Commerce Payments Api Association Type Example
  slug: commerce-payments-api-association-type-example
- key_count: 1
  name: Commerce Payments Api Batch Archive Request Example
  slug: commerce-payments-api-batch-archive-request-example
- key_count: 1
  name: Commerce Payments Api Batch Create Request Example
  slug: commerce-payments-api-batch-create-request-example
- key_count: 8
  name: Commerce Payments Api Batch Create Response Example
  slug: commerce-payments-api-batch-create-response-example
- key_count: 8
  name: Commerce Payments Api Batch Error Example
  slug: commerce-payments-api-batch-error-example
- key_count: 1
  name: Commerce Payments Api Batch Read Input Item Example
  slug: commerce-payments-api-batch-read-input-item-example
- key_count: 4
  name: Commerce Payments Api Batch Read Request Example
  slug: commerce-payments-api-batch-read-request-example
- key_count: 8
  name: Commerce Payments Api Batch Read Response Example
  slug: commerce-payments-api-batch-read-response-example
- key_count: 3
  name: Commerce Payments Api Batch Update Input Item Example
  slug: commerce-payments-api-batch-update-input-item-example
- key_count: 1
  name: Commerce Payments Api Batch Update Request Example
  slug: commerce-payments-api-batch-update-request-example
- key_count: 8
  name: Commerce Payments Api Batch Update Response Example
  slug: commerce-payments-api-batch-update-response-example
- key_count: 2
  name: Commerce Payments Api Commerce Payment Collection Example
  slug: commerce-payments-api-commerce-payment-collection-example
- key_count: 8
  name: Commerce Payments Api Commerce Payment Example
  slug: commerce-payments-api-commerce-payment-example
- key_count: 2
  name: Commerce Payments Api Commerce Payment Input Example
  slug: commerce-payments-api-commerce-payment-input-example
- key_count: 1
  name: Commerce Payments Api Commerce Payment Patch Example
  slug: commerce-payments-api-commerce-payment-patch-example
- key_count: 5
  name: Commerce Payments Api Filter Example
  slug: commerce-payments-api-filter-example
- key_count: 1
  name: Commerce Payments Api Filter Group Example
  slug: commerce-payments-api-filter-group-example
- key_count: 2
  name: Commerce Payments Api Paging Example
  slug: commerce-payments-api-paging-example
- key_count: 6
  name: Commerce Payments Api Property History Example
  slug: commerce-payments-api-property-history-example
- key_count: 6
  name: Commerce Payments Api Search Request Example
  slug: commerce-payments-api-search-request-example
- key_count: 3
  name: Commerce Payments Api Search Response Example
  slug: commerce-payments-api-search-response-example
- key_count: 2
  name: Commerce Payments Api Sort Option Example
  slug: commerce-payments-api-sort-option-example
- key_count: 2
  name: Commerce Subscriptions Api Association Example
  slug: commerce-subscriptions-api-association-example
- key_count: 1
  name: Commerce Subscriptions Api Batch Create Input Example
  slug: commerce-subscriptions-api-batch-create-input-example
- key_count: 2
  name: Commerce Subscriptions Api Batch Read Input Example
  slug: commerce-subscriptions-api-batch-read-input-example
- key_count: 3
  name: Commerce Subscriptions Api Batch Response Subscription Example
  slug: commerce-subscriptions-api-batch-response-subscription-example
- key_count: 1
  name: Commerce Subscriptions Api Batch Update Input Example
  slug: commerce-subscriptions-api-batch-update-input-example
- key_count: 2
  name: Commerce Subscriptions Api Collection Response Association Example
  slug: commerce-subscriptions-api-collection-response-association-example
- key_count: 2
  name: Commerce Subscriptions Api Collection Response Subscription Example
  slug: commerce-subscriptions-api-collection-response-subscription-example
- key_count: 3
  name: Commerce Subscriptions Api Filter Example
  slug: commerce-subscriptions-api-filter-example
- key_count: 1
  name: Commerce Subscriptions Api Filter Group Example
  slug: commerce-subscriptions-api-filter-group-example
- key_count: 1
  name: Commerce Subscriptions Api Paging Example
  slug: commerce-subscriptions-api-paging-example
- key_count: 6
  name: Commerce Subscriptions Api Search Request Example
  slug: commerce-subscriptions-api-search-request-example
- key_count: 1
  name: Commerce Subscriptions Api Simple Public Object Input Example
  slug: commerce-subscriptions-api-simple-public-object-input-example
- key_count: 6
  name: Commerce Subscriptions Api Subscription Example
  slug: commerce-subscriptions-api-subscription-example
- key_count: 2
  name: Conversations Api Actor Collection Example
  slug: conversations-api-actor-collection-example
- key_count: 5
  name: Conversations Api Actor Example
  slug: conversations-api-actor-example
- key_count: 5
  name: Conversations Api Attachment Example
  slug: conversations-api-attachment-example
- key_count: 2
  name: Conversations Api Channel Collection Example
  slug: conversations-api-channel-collection-example
- key_count: 5
  name: Conversations Api Channel Example
  slug: conversations-api-channel-example
- key_count: 3
  name: Conversations Api Inbox Collection Example
  slug: conversations-api-inbox-collection-example
- key_count: 6
  name: Conversations Api Inbox Example
  slug: conversations-api-inbox-example
- key_count: 2
  name: Conversations Api Message Collection Example
  slug: conversations-api-message-collection-example
- key_count: 13
  name: Conversations Api Message Example
  slug: conversations-api-message-example
- key_count: 1
  name: Conversations Api Message Recipient Example
  slug: conversations-api-message-recipient-example
- key_count: 1
  name: Conversations Api Message Status Example
  slug: conversations-api-message-status-example
- key_count: 1
  name: Conversations Api Paging Example
  slug: conversations-api-paging-example
- key_count: 2
  name: Conversations Api Paging Next Example
  slug: conversations-api-paging-next-example
- key_count: 7
  name: Conversations Api Send Message Request Example
  slug: conversations-api-send-message-request-example
- key_count: 2
  name: Conversations Api Thread Collection Example
  slug: conversations-api-thread-collection-example
- key_count: 14
  name: Conversations Api Thread Example
  slug: conversations-api-thread-example
- key_count: 2
  name: Conversations Api Update Thread Request Example
  slug: conversations-api-update-thread-request-example
- key_count: 2
  name: Crm Associations Api Association Definition Collection Example
  slug: crm-associations-api-association-definition-collection-example
- key_count: 7
  name: Crm Associations Api Association Definition Example
  slug: crm-associations-api-association-definition-example
- key_count: 2
  name: Crm Associations Api Association Example
  slug: crm-associations-api-association-example
- key_count: 2
  name: Crm Associations Api Association Label Collection Example
  slug: crm-associations-api-association-label-collection-example
- key_count: 3
  name: Crm Associations Api Association Label Example
  slug: crm-associations-api-association-label-example
- key_count: 3
  name: Crm Associations Api Association Result Example
  slug: crm-associations-api-association-result-example
- key_count: 3
  name: Crm Associations Api Association Type Example
  slug: crm-associations-api-association-type-example
- key_count: 2
  name: Crm Associations Api Association Type Input Example
  slug: crm-associations-api-association-type-input-example
- key_count: 1
  name: Crm Associations Api Batch Association Archive Input Example
  slug: crm-associations-api-batch-association-archive-input-example
- key_count: 3
  name: Crm Associations Api Batch Association Archive Item Example
  slug: crm-associations-api-batch-association-archive-item-example
- key_count: 1
  name: Crm Associations Api Batch Association Create Input Example
  slug: crm-associations-api-batch-association-create-input-example
- key_count: 3
  name: Crm Associations Api Batch Association Create Item Example
  slug: crm-associations-api-batch-association-create-item-example
- key_count: 1
  name: Crm Associations Api Batch Association Read Input Example
  slug: crm-associations-api-batch-association-read-input-example
- key_count: 8
  name: Crm Associations Api Batch Association Response Example
  slug: crm-associations-api-batch-association-response-example
- key_count: 2
  name: Crm Associations Api Create Association Input Example
  slug: crm-associations-api-create-association-input-example
- key_count: 3
  name: Crm Associations Api Create Label Input Example
  slug: crm-associations-api-create-label-input-example
- key_count: 1
  name: Crm Associations Api Object Reference Example
  slug: crm-associations-api-object-reference-example
- key_count: 1
  name: Crm Associations Api Paging Example
  slug: crm-associations-api-paging-example
- key_count: 2
  name: Crm Associations Api Paging Next Example
  slug: crm-associations-api-paging-next-example
- key_count: 2
  name: Crm Companies Api Association Example
  slug: crm-companies-api-association-example
- key_count: 1
  name: Crm Companies Api Batch Archive Input Example
  slug: crm-companies-api-batch-archive-input-example
- key_count: 1
  name: Crm Companies Api Batch Create Input Example
  slug: crm-companies-api-batch-create-input-example
- key_count: 2
  name: Crm Companies Api Batch Read Input Example
  slug: crm-companies-api-batch-read-input-example
- key_count: 3
  name: Crm Companies Api Batch Response Company Example
  slug: crm-companies-api-batch-response-company-example
- key_count: 1
  name: Crm Companies Api Batch Update Input Example
  slug: crm-companies-api-batch-update-input-example
- key_count: 2
  name: Crm Companies Api Collection Response Association Example
  slug: crm-companies-api-collection-response-association-example
- key_count: 2
  name: Crm Companies Api Collection Response Company Example
  slug: crm-companies-api-collection-response-company-example
- key_count: 6
  name: Crm Companies Api Company Example
  slug: crm-companies-api-company-example
- key_count: 3
  name: Crm Companies Api Filter Example
  slug: crm-companies-api-filter-example
- key_count: 1
  name: Crm Companies Api Filter Group Example
  slug: crm-companies-api-filter-group-example
- key_count: 1
  name: Crm Companies Api Paging Example
  slug: crm-companies-api-paging-example
- key_count: 6
  name: Crm Companies Api Search Request Example
  slug: crm-companies-api-search-request-example
- key_count: 1
  name: Crm Companies Api Simple Public Object Input Example
  slug: crm-companies-api-simple-public-object-input-example
- key_count: 2
  name: Crm Contacts Api Association Example
  slug: crm-contacts-api-association-example
- key_count: 1
  name: Crm Contacts Api Batch Archive Input Example
  slug: crm-contacts-api-batch-archive-input-example
- key_count: 1
  name: Crm Contacts Api Batch Create Input Example
  slug: crm-contacts-api-batch-create-input-example
- key_count: 2
  name: Crm Contacts Api Batch Read Input Example
  slug: crm-contacts-api-batch-read-input-example
- key_count: 3
  name: Crm Contacts Api Batch Response Contact Example
  slug: crm-contacts-api-batch-response-contact-example
- key_count: 1
  name: Crm Contacts Api Batch Update Input Example
  slug: crm-contacts-api-batch-update-input-example
- key_count: 2
  name: Crm Contacts Api Collection Response Association Example
  slug: crm-contacts-api-collection-response-association-example
- key_count: 2
  name: Crm Contacts Api Collection Response Contact Example
  slug: crm-contacts-api-collection-response-contact-example
- key_count: 6
  name: Crm Contacts Api Contact Example
  slug: crm-contacts-api-contact-example
- key_count: 3
  name: Crm Contacts Api Filter Example
  slug: crm-contacts-api-filter-example
- key_count: 1
  name: Crm Contacts Api Filter Group Example
  slug: crm-contacts-api-filter-group-example
- key_count: 1
  name: Crm Contacts Api Paging Example
  slug: crm-contacts-api-paging-example
- key_count: 6
  name: Crm Contacts Api Search Request Example
  slug: crm-contacts-api-search-request-example
- key_count: 1
  name: Crm Contacts Api Simple Public Object Input Example
  slug: crm-contacts-api-simple-public-object-input-example
- key_count: 2
  name: Crm Deals Api Association Example
  slug: crm-deals-api-association-example
- key_count: 1
  name: Crm Deals Api Batch Archive Input Example
  slug: crm-deals-api-batch-archive-input-example
- key_count: 1
  name: Crm Deals Api Batch Create Input Example
  slug: crm-deals-api-batch-create-input-example
- key_count: 2
  name: Crm Deals Api Batch Read Input Example
  slug: crm-deals-api-batch-read-input-example
- key_count: 3
  name: Crm Deals Api Batch Response Deal Example
  slug: crm-deals-api-batch-response-deal-example
- key_count: 1
  name: Crm Deals Api Batch Update Input Example
  slug: crm-deals-api-batch-update-input-example
- key_count: 2
  name: Crm Deals Api Collection Response Association Example
  slug: crm-deals-api-collection-response-association-example
- key_count: 2
  name: Crm Deals Api Collection Response Deal Example
  slug: crm-deals-api-collection-response-deal-example
- key_count: 6
  name: Crm Deals Api Deal Example
  slug: crm-deals-api-deal-example
- key_count: 3
  name: Crm Deals Api Filter Example
  slug: crm-deals-api-filter-example
- key_count: 1
  name: Crm Deals Api Filter Group Example
  slug: crm-deals-api-filter-group-example
- key_count: 1
  name: Crm Deals Api Paging Example
  slug: crm-deals-api-paging-example
- key_count: 6
  name: Crm Deals Api Search Request Example
  slug: crm-deals-api-search-request-example
- key_count: 1
  name: Crm Deals Api Simple Public Object Input Example
  slug: crm-deals-api-simple-public-object-input-example
- key_count: 1
  name: Crm Feature Flags Api Batch Delete Input Example
  slug: crm-feature-flags-api-batch-delete-input-example
- key_count: 1
  name: Crm Feature Flags Api Batch Delete Input Item Example
  slug: crm-feature-flags-api-batch-delete-input-item-example
- key_count: 4
  name: Crm Feature Flags Api Batch Error Example
  slug: crm-feature-flags-api-batch-error-example
- key_count: 1
  name: Crm Feature Flags Api Batch Portal Flag State Input Example
  slug: crm-feature-flags-api-batch-portal-flag-state-input-example
- key_count: 2
  name: Crm Feature Flags Api Batch Portal Flag State Input Item Example
  slug: crm-feature-flags-api-batch-portal-flag-state-input-item-example
- key_count: 4
  name: Crm Feature Flags Api Batch Portal Flag State Response Example
  slug: crm-feature-flags-api-batch-portal-flag-state-response-example
- key_count: 5
  name: Crm Feature Flags Api Batch Portal Flag State Response With Errors Example
  slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors-example
- key_count: 4
  name: Crm Feature Flags Api Feature Flag Example
  slug: crm-feature-flags-api-feature-flag-example
- key_count: 1
  name: Crm Feature Flags Api Feature Flag Input Example
  slug: crm-feature-flags-api-feature-flag-input-example
- key_count: 1
  name: Crm Feature Flags Api Paging Example
  slug: crm-feature-flags-api-paging-example
- key_count: 2
  name: Crm Feature Flags Api Paging Next Example
  slug: crm-feature-flags-api-paging-next-example
- key_count: 2
  name: Crm Feature Flags Api Portal Flag State Collection Example
  slug: crm-feature-flags-api-portal-flag-state-collection-example
- key_count: 4
  name: Crm Feature Flags Api Portal Flag State Example
  slug: crm-feature-flags-api-portal-flag-state-example
- key_count: 1
  name: Crm Feature Flags Api Portal Flag State Input Example
  slug: crm-feature-flags-api-portal-flag-state-input-example
- key_count: 2
  name: Crm Lists Api Collection Response List Example
  slug: crm-lists-api-collection-response-list-example
- key_count: 2
  name: Crm Lists Api Collection Response Membership Example
  slug: crm-lists-api-collection-response-membership-example
- key_count: 4
  name: Crm Lists Api List Create Request Example
  slug: crm-lists-api-list-create-request-example
- key_count: 9
  name: Crm Lists Api List Example
  slug: crm-lists-api-list-example
- key_count: 2
  name: Crm Lists Api Membership Change Request Example
  slug: crm-lists-api-membership-change-request-example
- key_count: 4
  name: Crm Lists Api Membership Change Response Example
  slug: crm-lists-api-membership-change-response-example
- key_count: 2
  name: Crm Lists Api Membership Example
  slug: crm-lists-api-membership-example
- key_count: 1
  name: Crm Lists Api Paging Example
  slug: crm-lists-api-paging-example
- key_count: 5
  name: Crm Search Api Crmobject Example
  slug: crm-search-api-crmobject-example
- key_count: 5
  name: Crm Search Api Filter Example
  slug: crm-search-api-filter-example
- key_count: 1
  name: Crm Search Api Filter Group Example
  slug: crm-search-api-filter-group-example
- key_count: 1
  name: Crm Search Api Paging Example
  slug: crm-search-api-paging-example
- key_count: 6
  name: Crm Search Api Search Request Example
  slug: crm-search-api-search-request-example
- key_count: 3
  name: Crm Search Api Search Response Example
  slug: crm-search-api-search-response-example
- key_count: 2
  name: Crm Search Api Sort Example
  slug: crm-search-api-sort-example
- key_count: 2
  name: Crm Tickets Api Association Example
  slug: crm-tickets-api-association-example
- key_count: 1
  name: Crm Tickets Api Batch Archive Input Example
  slug: crm-tickets-api-batch-archive-input-example
- key_count: 1
  name: Crm Tickets Api Batch Create Input Example
  slug: crm-tickets-api-batch-create-input-example
- key_count: 2
  name: Crm Tickets Api Batch Read Input Example
  slug: crm-tickets-api-batch-read-input-example
- key_count: 3
  name: Crm Tickets Api Batch Response Ticket Example
  slug: crm-tickets-api-batch-response-ticket-example
- key_count: 1
  name: Crm Tickets Api Batch Update Input Example
  slug: crm-tickets-api-batch-update-input-example
- key_count: 2
  name: Crm Tickets Api Collection Response Association Example
  slug: crm-tickets-api-collection-response-association-example
- key_count: 2
  name: Crm Tickets Api Collection Response Ticket Example
  slug: crm-tickets-api-collection-response-ticket-example
- key_count: 3
  name: Crm Tickets Api Filter Example
  slug: crm-tickets-api-filter-example
- key_count: 1
  name: Crm Tickets Api Filter Group Example
  slug: crm-tickets-api-filter-group-example
- key_count: 1
  name: Crm Tickets Api Paging Example
  slug: crm-tickets-api-paging-example
- key_count: 6
  name: Crm Tickets Api Search Request Example
  slug: crm-tickets-api-search-request-example
- key_count: 1
  name: Crm Tickets Api Simple Public Object Input Example
  slug: crm-tickets-api-simple-public-object-input-example
- key_count: 6
  name: Crm Tickets Api Ticket Example
  slug: crm-tickets-api-ticket-example
- key_count: 2
  name: Custom Workflow Actions Api Action Definition Collection Example
  slug: custom-workflow-actions-api-action-definition-collection-example
- key_count: 10
  name: Custom Workflow Actions Api Action Definition Example
  slug: custom-workflow-actions-api-action-definition-example
- key_count: 7
  name: Custom Workflow Actions Api Action Definition Input Example
  slug: custom-workflow-actions-api-action-definition-input-example
- key_count: 7
  name: Custom Workflow Actions Api Action Definition Patch Example
  slug: custom-workflow-actions-api-action-definition-patch-example
- key_count: 2
  name: Custom Workflow Actions Api Action Definition Revision Collection Example
  slug: custom-workflow-actions-api-action-definition-revision-collection-example
- key_count: 3
  name: Custom Workflow Actions Api Action Definition Revision Example
  slug: custom-workflow-actions-api-action-definition-revision-example
- key_count: 1
  name: Custom Workflow Actions Api Action Function Collection Example
  slug: custom-workflow-actions-api-action-function-collection-example
- key_count: 3
  name: Custom Workflow Actions Api Action Function Example
  slug: custom-workflow-actions-api-action-function-example
- key_count: 1
  name: Custom Workflow Actions Api Action Function Input Example
  slug: custom-workflow-actions-api-action-function-input-example
- key_count: 2
  name: Custom Workflow Actions Api Action Function Reference Example
  slug: custom-workflow-actions-api-action-function-reference-example
- key_count: 4
  name: Custom Workflow Actions Api Action Labels Example
  slug: custom-workflow-actions-api-action-labels-example
- key_count: 1
  name: Custom Workflow Actions Api Batch Callback Completion Request Example
  slug: custom-workflow-actions-api-batch-callback-completion-request-example
- key_count: 3
  name: Custom Workflow Actions Api Batch Callback Error Example
  slug: custom-workflow-actions-api-batch-callback-error-example
- key_count: 2
  name: Custom Workflow Actions Api Batch Callback Input Example
  slug: custom-workflow-actions-api-batch-callback-input-example
- key_count: 2
  name: Custom Workflow Actions Api Batch Callback Response Example
  slug: custom-workflow-actions-api-batch-callback-response-example
- key_count: 1
  name: Custom Workflow Actions Api Callback Completion Request Example
  slug: custom-workflow-actions-api-callback-completion-request-example
- key_count: 3
  name: Custom Workflow Actions Api Field Option Example
  slug: custom-workflow-actions-api-field-option-example
- key_count: 6
  name: Custom Workflow Actions Api Field Type Definition Example
  slug: custom-workflow-actions-api-field-type-definition-example
- key_count: 3
  name: Custom Workflow Actions Api Input Field Example
  slug: custom-workflow-actions-api-input-field-example
- key_count: 1
  name: Custom Workflow Actions Api Object Request Options Example
  slug: custom-workflow-actions-api-object-request-options-example
- key_count: 1
  name: Custom Workflow Actions Api Output Field Example
  slug: custom-workflow-actions-api-output-field-example
- key_count: 1
  name: Custom Workflow Actions Api Paging Example
  slug: custom-workflow-actions-api-paging-example
- key_count: 3
  name: Domains Api Domain Collection Response Example
  slug: domains-api-domain-collection-response-example
- key_count: 21
  name: Domains Api Domain Example
  slug: domains-api-domain-example
- key_count: 1
  name: Domains Api Forward Paging Example
  slug: domains-api-forward-paging-example
- key_count: 2
  name: Domains Api Next Page Example
  slug: domains-api-next-page-example
- key_count: 2
  name: Engagement Calls Api Association Input Example
  slug: engagement-calls-api-association-input-example
- key_count: 2
  name: Engagement Calls Api Association Type Example
  slug: engagement-calls-api-association-type-example
- key_count: 1
  name: Engagement Calls Api Batch Archive Calls Request Example
  slug: engagement-calls-api-batch-archive-calls-request-example
- key_count: 7
  name: Engagement Calls Api Batch Calls Response Example
  slug: engagement-calls-api-batch-calls-response-example
- key_count: 1
  name: Engagement Calls Api Batch Create Calls Request Example
  slug: engagement-calls-api-batch-create-calls-request-example
- key_count: 5
  name: Engagement Calls Api Batch Error Example
  slug: engagement-calls-api-batch-error-example
- key_count: 4
  name: Engagement Calls Api Batch Read Calls Request Example
  slug: engagement-calls-api-batch-read-calls-request-example
- key_count: 1
  name: Engagement Calls Api Batch Read Input Example
  slug: engagement-calls-api-batch-read-input-example
- key_count: 1
  name: Engagement Calls Api Batch Update Calls Request Example
  slug: engagement-calls-api-batch-update-calls-request-example
- key_count: 2
  name: Engagement Calls Api Batch Update Input Example
  slug: engagement-calls-api-batch-update-input-example
- key_count: 2
  name: Engagement Calls Api Call Collection Response Example
  slug: engagement-calls-api-call-collection-response-example
- key_count: 2
  name: Engagement Calls Api Call Create Request Example
  slug: engagement-calls-api-call-create-request-example
- key_count: 7
  name: Engagement Calls Api Call Example
  slug: engagement-calls-api-call-example
- key_count: 6
  name: Engagement Calls Api Call Search Request Example
  slug: engagement-calls-api-call-search-request-example
- key_count: 3
  name: Engagement Calls Api Call Search Response Example
  slug: engagement-calls-api-call-search-response-example
- key_count: 1
  name: Engagement Calls Api Call Update Request Example
  slug: engagement-calls-api-call-update-request-example
- key_count: 5
  name: Engagement Calls Api Filter Example
  slug: engagement-calls-api-filter-example
- key_count: 1
  name: Engagement Calls Api Filter Group Example
  slug: engagement-calls-api-filter-group-example
- key_count: 2
  name: Engagement Calls Api Gdpr Delete Request Example
  slug: engagement-calls-api-gdpr-delete-request-example
- key_count: 2
  name: Engagement Calls Api Next Page Example
  slug: engagement-calls-api-next-page-example
- key_count: 1
  name: Engagement Calls Api Paging Example
  slug: engagement-calls-api-paging-example
- key_count: 6
  name: Engagement Calls Api Property History Example
  slug: engagement-calls-api-property-history-example
- key_count: 2
  name: Engagement Calls Api Sort Option Example
  slug: engagement-calls-api-sort-option-example
- key_count: 2
  name: Engagement Emails Api Association Example
  slug: engagement-emails-api-association-example
- key_count: 1
  name: Engagement Emails Api Batch Create Input Example
  slug: engagement-emails-api-batch-create-input-example
- key_count: 2
  name: Engagement Emails Api Batch Read Input Example
  slug: engagement-emails-api-batch-read-input-example
- key_count: 3
  name: Engagement Emails Api Batch Response Email Engagement Example
  slug: engagement-emails-api-batch-response-email-engagement-example
- key_count: 1
  name: Engagement Emails Api Batch Update Input Example
  slug: engagement-emails-api-batch-update-input-example
- key_count: 2
  name: Engagement Emails Api Collection Response Association Example
  slug: engagement-emails-api-collection-response-association-example
- key_count: 2
  name: Engagement Emails Api Collection Response Email Engagement Example
  slug: engagement-emails-api-collection-response-email-engagement-example
- key_count: 6
  name: Engagement Emails Api Email Engagement Example
  slug: engagement-emails-api-email-engagement-example
- key_count: 3
  name: Engagement Emails Api Filter Example
  slug: engagement-emails-api-filter-example
- key_count: 1
  name: Engagement Emails Api Filter Group Example
  slug: engagement-emails-api-filter-group-example
- key_count: 1
  name: Engagement Emails Api Paging Example
  slug: engagement-emails-api-paging-example
- key_count: 6
  name: Engagement Emails Api Search Request Example
  slug: engagement-emails-api-search-request-example
- key_count: 1
  name: Engagement Emails Api Simple Public Object Input Example
  slug: engagement-emails-api-simple-public-object-input-example
- key_count: 2
  name: Engagement Meetings Api Association Example
  slug: engagement-meetings-api-association-example
- key_count: 1
  name: Engagement Meetings Api Batch Create Input Example
  slug: engagement-meetings-api-batch-create-input-example
- key_count: 2
  name: Engagement Meetings Api Batch Read Input Example
  slug: engagement-meetings-api-batch-read-input-example
- key_count: 3
  name: Engagement Meetings Api Batch Response Meeting Example
  slug: engagement-meetings-api-batch-response-meeting-example
- key_count: 1
  name: Engagement Meetings Api Batch Update Input Example
  slug: engagement-meetings-api-batch-update-input-example
- key_count: 2
  name: Engagement Meetings Api Collection Response Association Example
  slug: engagement-meetings-api-collection-response-association-example
- key_count: 2
  name: Engagement Meetings Api Collection Response Meeting Example
  slug: engagement-meetings-api-collection-response-meeting-example
- key_count: 3
  name: Engagement Meetings Api Filter Example
  slug: engagement-meetings-api-filter-example
- key_count: 1
  name: Engagement Meetings Api Filter Group Example
  slug: engagement-meetings-api-filter-group-example
- key_count: 6
  name: Engagement Meetings Api Meeting Example
  slug: engagement-meetings-api-meeting-example
- key_count: 1
  name: Engagement Meetings Api Paging Example
  slug: engagement-meetings-api-paging-example
- key_count: 6
  name: Engagement Meetings Api Search Request Example
  slug: engagement-meetings-api-search-request-example
- key_count: 1
  name: Engagement Meetings Api Simple Public Object Input Example
  slug: engagement-meetings-api-simple-public-object-input-example
- key_count: 2
  name: Engagement Notes Association Input Example
  slug: engagement-notes-association-input-example
- key_count: 2
  name: Engagement Notes Association Type Example
  slug: engagement-notes-association-type-example
- key_count: 1
  name: Engagement Notes Batch Archive Notes Request Example
  slug: engagement-notes-batch-archive-notes-request-example
- key_count: 1
  name: Engagement Notes Batch Create Notes Request Example
  slug: engagement-notes-batch-create-notes-request-example
- key_count: 5
  name: Engagement Notes Batch Error Example
  slug: engagement-notes-batch-error-example
- key_count: 7
  name: Engagement Notes Batch Notes Response Example
  slug: engagement-notes-batch-notes-response-example
- key_count: 1
  name: Engagement Notes Batch Read Input Example
  slug: engagement-notes-batch-read-input-example
- key_count: 4
  name: Engagement Notes Batch Read Notes Request Example
  slug: engagement-notes-batch-read-notes-request-example
- key_count: 2
  name: Engagement Notes Batch Update Input Example
  slug: engagement-notes-batch-update-input-example
- key_count: 1
  name: Engagement Notes Batch Update Notes Request Example
  slug: engagement-notes-batch-update-notes-request-example
- key_count: 5
  name: Engagement Notes Filter Example
  slug: engagement-notes-filter-example
- key_count: 1
  name: Engagement Notes Filter Group Example
  slug: engagement-notes-filter-group-example
- key_count: 2
  name: Engagement Notes Gdpr Delete Request Example
  slug: engagement-notes-gdpr-delete-request-example
- key_count: 2
  name: Engagement Notes Next Page Example
  slug: engagement-notes-next-page-example
- key_count: 2
  name: Engagement Notes Note Collection Response Example
  slug: engagement-notes-note-collection-response-example
- key_count: 2
  name: Engagement Notes Note Create Request Example
  slug: engagement-notes-note-create-request-example
- key_count: 7
  name: Engagement Notes Note Example
  slug: engagement-notes-note-example
- key_count: 6
  name: Engagement Notes Note Search Request Example
  slug: engagement-notes-note-search-request-example
- key_count: 3
  name: Engagement Notes Note Search Response Example
  slug: engagement-notes-note-search-response-example
- key_count: 1
  name: Engagement Notes Note Update Request Example
  slug: engagement-notes-note-update-request-example
- key_count: 1
  name: Engagement Notes Paging Example
  slug: engagement-notes-paging-example
- key_count: 6
  name: Engagement Notes Property History Example
  slug: engagement-notes-property-history-example
- key_count: 2
  name: Engagement Notes Sort Option Example
  slug: engagement-notes-sort-option-example
- key_count: 2
  name: Engagement Tasks Api Association Example
  slug: engagement-tasks-api-association-example
- key_count: 1
  name: Engagement Tasks Api Batch Create Input Example
  slug: engagement-tasks-api-batch-create-input-example
- key_count: 2
  name: Engagement Tasks Api Batch Read Input Example
  slug: engagement-tasks-api-batch-read-input-example
- key_count: 3
  name: Engagement Tasks Api Batch Response Task Example
  slug: engagement-tasks-api-batch-response-task-example
- key_count: 1
  name: Engagement Tasks Api Batch Update Input Example
  slug: engagement-tasks-api-batch-update-input-example
- key_count: 2
  name: Engagement Tasks Api Collection Response Association Example
  slug: engagement-tasks-api-collection-response-association-example
- key_count: 2
  name: Engagement Tasks Api Collection Response Task Example
  slug: engagement-tasks-api-collection-response-task-example
- key_count: 3
  name: Engagement Tasks Api Filter Example
  slug: engagement-tasks-api-filter-example
- key_count: 1
  name: Engagement Tasks Api Filter Group Example
  slug: engagement-tasks-api-filter-group-example
- key_count: 1
  name: Engagement Tasks Api Paging Example
  slug: engagement-tasks-api-paging-example
- key_count: 6
  name: Engagement Tasks Api Search Request Example
  slug: engagement-tasks-api-search-request-example
- key_count: 1
  name: Engagement Tasks Api Simple Public Object Input Example
  slug: engagement-tasks-api-simple-public-object-input-example
- key_count: 6
  name: Engagement Tasks Api Task Example
  slug: engagement-tasks-api-task-example
- key_count: 5
  name: Hubspot Analytics Events Error Detail Example
  slug: hubspot-analytics-events-error-detail-example
- key_count: 7
  name: Hubspot Analytics Events Error Example
  slug: hubspot-analytics-events-error-example
- key_count: 2
  name: Hubspot Analytics Events Event Instance Collection Example
  slug: hubspot-analytics-events-event-instance-collection-example
- key_count: 6
  name: Hubspot Analytics Events Event Instance Example
  slug: hubspot-analytics-events-event-instance-example
- key_count: 1
  name: Hubspot Analytics Events Event Type Collection Example
  slug: hubspot-analytics-events-event-type-collection-example
- key_count: 2
  name: Hubspot Analytics Events Paging Example
  slug: hubspot-analytics-events-paging-example
- key_count: 2
  name: Hubspot Analytics Events Paging Next Example
  slug: hubspot-analytics-events-paging-next-example
- key_count: 2
  name: Hubspot Analytics Events Paging Previous Example
  slug: hubspot-analytics-events-paging-previous-example
- key_count: 4
  name: Hubspot Authors Attach To Language Group Request Example
  slug: hubspot-authors-attach-to-language-group-request-example
- key_count: 1
  name: Hubspot Authors Batch Archive Input Example
  slug: hubspot-authors-batch-archive-input-example
- key_count: 1
  name: Hubspot Authors Batch Create Input Example
  slug: hubspot-authors-batch-create-input-example
- key_count: 1
  name: Hubspot Authors Batch Input Example
  slug: hubspot-authors-batch-input-example
- key_count: 2
  name: Hubspot Authors Batch Input Item Example
  slug: hubspot-authors-batch-input-item-example
- key_count: 1
  name: Hubspot Authors Batch Read Input Example
  slug: hubspot-authors-batch-read-input-example
- key_count: 6
  name: Hubspot Authors Batch Response Example
  slug: hubspot-authors-batch-response-example
- key_count: 0
  name: Hubspot Authors Batch Response With Errors Example
  slug: hubspot-authors-batch-response-with-errors-example
- key_count: 3
  name: Hubspot Authors Blog Author Collection Example
  slug: hubspot-authors-blog-author-collection-example
- key_count: 15
  name: Hubspot Authors Blog Author Example
  slug: hubspot-authors-blog-author-example
- key_count: 9
  name: Hubspot Authors Blog Author Input Example
  slug: hubspot-authors-blog-author-input-example
- key_count: 2
  name: Hubspot Authors Create Language Variation Request Example
  slug: hubspot-authors-create-language-variation-request-example
- key_count: 1
  name: Hubspot Authors Detach From Language Group Request Example
  slug: hubspot-authors-detach-from-language-group-request-example
- key_count: 5
  name: Hubspot Authors Error Detail Example
  slug: hubspot-authors-error-detail-example
- key_count: 7
  name: Hubspot Authors Error Example
  slug: hubspot-authors-error-example
- key_count: 1
  name: Hubspot Authors Paging Example
  slug: hubspot-authors-paging-example
- key_count: 2
  name: Hubspot Authors Paging Next Example
  slug: hubspot-authors-paging-next-example
- key_count: 1
  name: Hubspot Authors Set Language Primary Request Example
  slug: hubspot-authors-set-language-primary-request-example
- key_count: 7
  name: Hubspot Authors Standard Error Example
  slug: hubspot-authors-standard-error-example
- key_count: 4
  name: Hubspot Blog Posts Attach To Language Group Request Example
  slug: hubspot-blog-posts-attach-to-language-group-request-example
- key_count: 1
  name: Hubspot Blog Posts Batch Input Example
  slug: hubspot-blog-posts-batch-input-example
- key_count: 1
  name: Hubspot Blog Posts Batch Input Item Example
  slug: hubspot-blog-posts-batch-input-item-example
- key_count: 6
  name: Hubspot Blog Posts Batch Response Example
  slug: hubspot-blog-posts-batch-response-example
- key_count: 0
  name: Hubspot Blog Posts Batch Response With Errors Example
  slug: hubspot-blog-posts-batch-response-with-errors-example
- key_count: 3
  name: Hubspot Blog Posts Blog Post Collection Example
  slug: hubspot-blog-posts-blog-post-collection-example
- key_count: 32
  name: Hubspot Blog Posts Blog Post Example
  slug: hubspot-blog-posts-blog-post-example
- key_count: 15
  name: Hubspot Blog Posts Blog Post Input Example
  slug: hubspot-blog-posts-blog-post-input-example
- key_count: 1
  name: Hubspot Blog Posts Clone Request Example
  slug: hubspot-blog-posts-clone-request-example
- key_count: 2
  name: Hubspot Blog Posts Create Language Variation Request Example
  slug: hubspot-blog-posts-create-language-variation-request-example
- key_count: 1
  name: Hubspot Blog Posts Detach From Language Group Request Example
  slug: hubspot-blog-posts-detach-from-language-group-request-example
- key_count: 5
  name: Hubspot Blog Posts Error Detail Example
  slug: hubspot-blog-posts-error-detail-example
- key_count: 7
  name: Hubspot Blog Posts Error Example
  slug: hubspot-blog-posts-error-example
- key_count: 2
  name: Hubspot Blog Posts Paging Example
  slug: hubspot-blog-posts-paging-example
- key_count: 2
  name: Hubspot Blog Posts Paging Next Example
  slug: hubspot-blog-posts-paging-next-example
- key_count: 2
  name: Hubspot Blog Posts Paging Previous Example
  slug: hubspot-blog-posts-paging-previous-example
- key_count: 1
  name: Hubspot Blog Posts Push Live Request Example
  slug: hubspot-blog-posts-push-live-request-example
- key_count: 1
  name: Hubspot Blog Posts Reset Draft Request Example
  slug: hubspot-blog-posts-reset-draft-request-example
- key_count: 2
  name: Hubspot Blog Posts Restore Previous Version Request Example
  slug: hubspot-blog-posts-restore-previous-version-request-example
- key_count: 2
  name: Hubspot Blog Posts Schedule Request Example
  slug: hubspot-blog-posts-schedule-request-example
- key_count: 1
  name: Hubspot Blog Posts Set Language Primary Request Example
  slug: hubspot-blog-posts-set-language-primary-request-example
- key_count: 7
  name: Hubspot Blog Posts Standard Error Example
  slug: hubspot-blog-posts-standard-error-example
- key_count: 4
  name: Hubspot Blog Posts Version History Example
  slug: hubspot-blog-posts-version-history-example
- key_count: 2
  name: Hubspot Cms Hubdb Collection Response Hub Db Row Example
  slug: hubspot-cms-hubdb-collection-response-hub-db-row-example
- key_count: 2
  name: Hubspot Cms Hubdb Collection Response Hub Db Table Example
  slug: hubspot-cms-hubdb-collection-response-hub-db-table-example
- key_count: 4
  name: Hubspot Cms Hubdb Error Example
  slug: hubspot-cms-hubdb-error-example
- key_count: 5
  name: Hubspot Cms Hubdb Hub Db Column Example
  slug: hubspot-cms-hubdb-hub-db-column-example
- key_count: 1
  name: Hubspot Cms Hubdb Hub Db Row Create Request Example
  slug: hubspot-cms-hubdb-hub-db-row-create-request-example
- key_count: 4
  name: Hubspot Cms Hubdb Hub Db Row Example
  slug: hubspot-cms-hubdb-hub-db-row-example
- key_count: 3
  name: Hubspot Cms Hubdb Hub Db Table Create Request Example
  slug: hubspot-cms-hubdb-hub-db-table-create-request-example
- key_count: 9
  name: Hubspot Cms Hubdb Hub Db Table Example
  slug: hubspot-cms-hubdb-hub-db-table-example
- key_count: 1
  name: Hubspot Cms Hubdb Paging Example
  slug: hubspot-cms-hubdb-paging-example
- key_count: 2
  name: Hubspot Cms Pages Collection Response Page Example
  slug: hubspot-cms-pages-collection-response-page-example
- key_count: 4
  name: Hubspot Cms Pages Error Example
  slug: hubspot-cms-pages-error-example
- key_count: 8
  name: Hubspot Cms Pages Page Create Request Example
  slug: hubspot-cms-pages-page-create-request-example
- key_count: 16
  name: Hubspot Cms Pages Page Example
  slug: hubspot-cms-pages-page-example
- key_count: 5
  name: Hubspot Cms Pages Page Update Request Example
  slug: hubspot-cms-pages-page-update-request-example
- key_count: 1
  name: Hubspot Cms Pages Paging Example
  slug: hubspot-cms-pages-paging-example
- key_count: 2
  name: Hubspot Commerce Payments Association Input Example
  slug: hubspot-commerce-payments-association-input-example
- key_count: 2
  name: Hubspot Commerce Payments Association Result Example
  slug: hubspot-commerce-payments-association-result-example
- key_count: 2
  name: Hubspot Commerce Payments Association Type Example
  slug: hubspot-commerce-payments-association-type-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Archive Request Example
  slug: hubspot-commerce-payments-batch-archive-request-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Create Request Example
  slug: hubspot-commerce-payments-batch-create-request-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Create Response Example
  slug: hubspot-commerce-payments-batch-create-response-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Error Example
  slug: hubspot-commerce-payments-batch-error-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Read Input Item Example
  slug: hubspot-commerce-payments-batch-read-input-item-example
- key_count: 4
  name: Hubspot Commerce Payments Batch Read Request Example
  slug: hubspot-commerce-payments-batch-read-request-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Read Response Example
  slug: hubspot-commerce-payments-batch-read-response-example
- key_count: 3
  name: Hubspot Commerce Payments Batch Update Input Item Example
  slug: hubspot-commerce-payments-batch-update-input-item-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Update Request Example
  slug: hubspot-commerce-payments-batch-update-request-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Update Response Example
  slug: hubspot-commerce-payments-batch-update-response-example
- key_count: 2
  name: Hubspot Commerce Payments Commerce Payment Collection Example
  slug: hubspot-commerce-payments-commerce-payment-collection-example
- key_count: 8
  name: Hubspot Commerce Payments Commerce Payment Example
  slug: hubspot-commerce-payments-commerce-payment-example
- key_count: 2
  name: Hubspot Commerce Payments Commerce Payment Input Example
  slug: hubspot-commerce-payments-commerce-payment-input-example
- key_count: 1
  name: Hubspot Commerce Payments Commerce Payment Patch Example
  slug: hubspot-commerce-payments-commerce-payment-patch-example
- key_count: 5
  name: Hubspot Commerce Payments Error Detail Example
  slug: hubspot-commerce-payments-error-detail-example
- key_count: 7
  name: Hubspot Commerce Payments Error Example
  slug: hubspot-commerce-payments-error-example
- key_count: 5
  name: Hubspot Commerce Payments Filter Example
  slug: hubspot-commerce-payments-filter-example
- key_count: 1
  name: Hubspot Commerce Payments Filter Group Example
  slug: hubspot-commerce-payments-filter-group-example
- key_count: 2
  name: Hubspot Commerce Payments Paging Example
  slug: hubspot-commerce-payments-paging-example
- key_count: 6
  name: Hubspot Commerce Payments Property History Example
  slug: hubspot-commerce-payments-property-history-example
- key_count: 6
  name: Hubspot Commerce Payments Search Request Example
  slug: hubspot-commerce-payments-search-request-example
- key_count: 3
  name: Hubspot Commerce Payments Search Response Example
  slug: hubspot-commerce-payments-search-response-example
- key_count: 2
  name: Hubspot Commerce Payments Sort Option Example
  slug: hubspot-commerce-payments-sort-option-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Association Example
  slug: hubspot-commerce-subscriptions-association-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Batch Create Input Example
  slug: hubspot-commerce-subscriptions-batch-create-input-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Batch Read Input Example
  slug: hubspot-commerce-subscriptions-batch-read-input-example
- key_count: 3
  name: Hubspot Commerce Subscriptions Batch Response Subscription Example
  slug: hubspot-commerce-subscriptions-batch-response-subscription-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Batch Update Input Example
  slug: hubspot-commerce-subscriptions-batch-update-input-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Collection Response Association Example
  slug: hubspot-commerce-subscriptions-collection-response-association-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Collection Response Subscription Example
  slug: hubspot-commerce-subscriptions-collection-response-subscription-example
- key_count: 4
  name: Hubspot Commerce Subscriptions Error Example
  slug: hubspot-commerce-subscriptions-error-example
- key_count: 3
  name: Hubspot Commerce Subscriptions Filter Example
  slug: hubspot-commerce-subscriptions-filter-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Filter Group Example
  slug: hubspot-commerce-subscriptions-filter-group-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Paging Example
  slug: hubspot-commerce-subscriptions-paging-example
- key_count: 6
  name: Hubspot Commerce Subscriptions Search Request Example
  slug: hubspot-commerce-subscriptions-search-request-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Simple Public Object Input Example
  slug: hubspot-commerce-subscriptions-simple-public-object-input-example
- key_count: 6
  name: Hubspot Commerce Subscriptions Subscription Example
  slug: hubspot-commerce-subscriptions-subscription-example
- key_count: 2
  name: Hubspot Conversations Actor Collection Example
  slug: hubspot-conversations-actor-collection-example
- key_count: 5
  name: Hubspot Conversations Actor Example
  slug: hubspot-conversations-actor-example
- key_count: 5
  name: Hubspot Conversations Attachment Example
  slug: hubspot-conversations-attachment-example
- key_count: 2
  name: Hubspot Conversations Channel Collection Example
  slug: hubspot-conversations-channel-collection-example
- key_count: 5
  name: Hubspot Conversations Channel Example
  slug: hubspot-conversations-channel-example
- key_count: 5
  name: Hubspot Conversations Error Detail Example
  slug: hubspot-conversations-error-detail-example
- key_count: 7
  name: Hubspot Conversations Error Example
  slug: hubspot-conversations-error-example
- key_count: 3
  name: Hubspot Conversations Inbox Collection Example
  slug: hubspot-conversations-inbox-collection-example
- key_count: 6
  name: Hubspot Conversations Inbox Example
  slug: hubspot-conversations-inbox-example
- key_count: 2
  name: Hubspot Conversations Message Collection Example
  slug: hubspot-conversations-message-collection-example
- key_count: 13
  name: Hubspot Conversations Message Example
  slug: hubspot-conversations-message-example
- key_count: 1
  name: Hubspot Conversations Message Recipient Example
  slug: hubspot-conversations-message-recipient-example
- key_count: 1
  name: Hubspot Conversations Message Status Example
  slug: hubspot-conversations-message-status-example
- key_count: 1
  name: Hubspot Conversations Paging Example
  slug: hubspot-conversations-paging-example
- key_count: 2
  name: Hubspot Conversations Paging Next Example
  slug: hubspot-conversations-paging-next-example
- key_count: 7
  name: Hubspot Conversations Send Message Request Example
  slug: hubspot-conversations-send-message-request-example
- key_count: 2
  name: Hubspot Conversations Thread Collection Example
  slug: hubspot-conversations-thread-collection-example
- key_count: 14
  name: Hubspot Conversations Thread Example
  slug: hubspot-conversations-thread-example
- key_count: 2
  name: Hubspot Conversations Update Thread Request Example
  slug: hubspot-conversations-update-thread-request-example
- key_count: 2
  name: Hubspot Crm Associations Association Definition Collection Example
  slug: hubspot-crm-associations-association-definition-collection-example
- key_count: 7
  name: Hubspot Crm Associations Association Definition Example
  slug: hubspot-crm-associations-association-definition-example
- key_count: 2
  name: Hubspot Crm Associations Association Example
  slug: hubspot-crm-associations-association-example
- key_count: 2
  name: Hubspot Crm Associations Association Label Collection Example
  slug: hubspot-crm-associations-association-label-collection-example
- key_count: 3
  name: Hubspot Crm Associations Association Label Example
  slug: hubspot-crm-associations-association-label-example
- key_count: 3
  name: Hubspot Crm Associations Association Result Example
  slug: hubspot-crm-associations-association-result-example
- key_count: 3
  name: Hubspot Crm Associations Association Type Example
  slug: hubspot-crm-associations-association-type-example
- key_count: 2
  name: Hubspot Crm Associations Association Type Input Example
  slug: hubspot-crm-associations-association-type-input-example
- key_count: 1
  name: Hubspot Crm Associations Batch Association Archive Input Example
  slug: hubspot-crm-associations-batch-association-archive-input-example
- key_count: 3
  name: Hubspot Crm Associations Batch Association Archive Item Example
  slug: hubspot-crm-associations-batch-association-archive-item-example
- key_count: 1
  name: Hubspot Crm Associations Batch Association Create Input Example
  slug: hubspot-crm-associations-batch-association-create-input-example
- key_count: 3
  name: Hubspot Crm Associations Batch Association Create Item Example
  slug: hubspot-crm-associations-batch-association-create-item-example
- key_count: 1
  name: Hubspot Crm Associations Batch Association Read Input Example
  slug: hubspot-crm-associations-batch-association-read-input-example
- key_count: 8
  name: Hubspot Crm Associations Batch Association Response Example
  slug: hubspot-crm-associations-batch-association-response-example
- key_count: 2
  name: Hubspot Crm Associations Create Association Input Example
  slug: hubspot-crm-associations-create-association-input-example
- key_count: 3
  name: Hubspot Crm Associations Create Label Input Example
  slug: hubspot-crm-associations-create-label-input-example
- key_count: 5
  name: Hubspot Crm Associations Error Detail Example
  slug: hubspot-crm-associations-error-detail-example
- key_count: 7
  name: Hubspot Crm Associations Error Example
  slug: hubspot-crm-associations-error-example
- key_count: 1
  name: Hubspot Crm Associations Object Reference Example
  slug: hubspot-crm-associations-object-reference-example
- key_count: 1
  name: Hubspot Crm Associations Paging Example
  slug: hubspot-crm-associations-paging-example
- key_count: 2
  name: Hubspot Crm Associations Paging Next Example
  slug: hubspot-crm-associations-paging-next-example
- key_count: 7
  name: Hubspot Crm Associations Standard Error Example
  slug: hubspot-crm-associations-standard-error-example
- key_count: 2
  name: Hubspot Crm Companies Association Example
  slug: hubspot-crm-companies-association-example
- key_count: 1
  name: Hubspot Crm Companies Batch Archive Input Example
  slug: hubspot-crm-companies-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Companies Batch Create Input Example
  slug: hubspot-crm-companies-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Companies Batch Read Input Example
  slug: hubspot-crm-companies-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Companies Batch Response Company Example
  slug: hubspot-crm-companies-batch-response-company-example
- key_count: 1
  name: Hubspot Crm Companies Batch Update Input Example
  slug: hubspot-crm-companies-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Companies Collection Response Association Example
  slug: hubspot-crm-companies-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Companies Collection Response Company Example
  slug: hubspot-crm-companies-collection-response-company-example
- key_count: 6
  name: Hubspot Crm Companies Company Example
  slug: hubspot-crm-companies-company-example
- key_count: 4
  name: Hubspot Crm Companies Error Example
  slug: hubspot-crm-companies-error-example
- key_count: 3
  name: Hubspot Crm Companies Filter Example
  slug: hubspot-crm-companies-filter-example
- key_count: 1
  name: Hubspot Crm Companies Filter Group Example
  slug: hubspot-crm-companies-filter-group-example
- key_count: 1
  name: Hubspot Crm Companies Paging Example
  slug: hubspot-crm-companies-paging-example
- key_count: 6
  name: Hubspot Crm Companies Search Request Example
  slug: hubspot-crm-companies-search-request-example
- key_count: 1
  name: Hubspot Crm Companies Simple Public Object Input Example
  slug: hubspot-crm-companies-simple-public-object-input-example
- key_count: 2
  name: Hubspot Crm Contacts Association Example
  slug: hubspot-crm-contacts-association-example
- key_count: 1
  name: Hubspot Crm Contacts Batch Archive Input Example
  slug: hubspot-crm-contacts-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Contacts Batch Create Input Example
  slug: hubspot-crm-contacts-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Contacts Batch Read Input Example
  slug: hubspot-crm-contacts-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Contacts Batch Response Contact Example
  slug: hubspot-crm-contacts-batch-response-contact-example
- key_count: 1
  name: Hubspot Crm Contacts Batch Update Input Example
  slug: hubspot-crm-contacts-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Contacts Collection Response Association Example
  slug: hubspot-crm-contacts-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Contacts Collection Response Contact Example
  slug: hubspot-crm-contacts-collection-response-contact-example
- key_count: 6
  name: Hubspot Crm Contacts Contact Example
  slug: hubspot-crm-contacts-contact-example
- key_count: 4
  name: Hubspot Crm Contacts Error Example
  slug: hubspot-crm-contacts-error-example
- key_count: 3
  name: Hubspot Crm Contacts Filter Example
  slug: hubspot-crm-contacts-filter-example
- key_count: 1
  name: Hubspot Crm Contacts Filter Group Example
  slug: hubspot-crm-contacts-filter-group-example
- key_count: 1
  name: Hubspot Crm Contacts Paging Example
  slug: hubspot-crm-contacts-paging-example
- key_count: 6
  name: Hubspot Crm Contacts Search Request Example
  slug: hubspot-crm-contacts-search-request-example
- key_count: 1
  name: Hubspot Crm Contacts Simple Public Object Input Example
  slug: hubspot-crm-contacts-simple-public-object-input-example
- key_count: 2
  name: Hubspot Crm Deals Association Example
  slug: hubspot-crm-deals-association-example
- key_count: 1
  name: Hubspot Crm Deals Batch Archive Input Example
  slug: hubspot-crm-deals-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Deals Batch Create Input Example
  slug: hubspot-crm-deals-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Deals Batch Read Input Example
  slug: hubspot-crm-deals-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Deals Batch Response Deal Example
  slug: hubspot-crm-deals-batch-response-deal-example
- key_count: 1
  name: Hubspot Crm Deals Batch Update Input Example
  slug: hubspot-crm-deals-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Deals Collection Response Association Example
  slug: hubspot-crm-deals-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Deals Collection Response Deal Example
  slug: hubspot-crm-deals-collection-response-deal-example
- key_count: 6
  name: Hubspot Crm Deals Deal Example
  slug: hubspot-crm-deals-deal-example
- key_count: 4
  name: Hubspot Crm Deals Error Example
  slug: hubspot-crm-deals-error-example
- key_count: 3
  name: Hubspot Crm Deals Filter Example
  slug: hubspot-crm-deals-filter-example
- key_count: 1
  name: Hubspot Crm Deals Filter Group Example
  slug: hubspot-crm-deals-filter-group-example
- key_count: 1
  name: Hubspot Crm Deals Paging Example
  slug: hubspot-crm-deals-paging-example
- key_count: 6
  name: Hubspot Crm Deals Search Request Example
  slug: hubspot-crm-deals-search-request-example
- key_count: 1
  name: Hubspot Crm Deals Simple Public Object Input Example
  slug: hubspot-crm-deals-simple-public-object-input-example
- key_count: 1
  name: Hubspot Crm Feature Flags Batch Delete Input Example
  slug: hubspot-crm-feature-flags-batch-delete-input-example
- key_count: 1
  name: Hubspot Crm Feature Flags Batch Delete Input Item Example
  slug: hubspot-crm-feature-flags-batch-delete-input-item-example
- key_count: 4
  name: Hubspot Crm Feature Flags Batch Error Example
  slug: hubspot-crm-feature-flags-batch-error-example
- key_count: 1
  name: Hubspot Crm Feature Flags Batch Portal Flag State Input Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-example
- key_count: 2
  name: Hubspot Crm Feature Flags Batch Portal Flag State Input Item Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-item-example
- key_count: 4
  name: Hubspot Crm Feature Flags Batch Portal Flag State Response Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-example
- key_count: 5
  name: Hubspot Crm Feature Flags Batch Portal Flag State Response With Errors Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-with-errors-example
- key_count: 5
  name: Hubspot Crm Feature Flags Error Detail Example
  slug: hubspot-crm-feature-flags-error-detail-example
- key_count: 7
  name: Hubspot Crm Feature Flags Error Example
  slug: hubspot-crm-feature-flags-error-example
- key_count: 4
  name: Hubspot Crm Feature Flags Feature Flag Example
  slug: hubspot-crm-feature-flags-feature-flag-example
- key_count: 1
  name: Hubspot Crm Feature Flags Feature Flag Input Example
  slug: hubspot-crm-feature-flags-feature-flag-input-example
- key_count: 1
  name: Hubspot Crm Feature Flags Paging Example
  slug: hubspot-crm-feature-flags-paging-example
- key_count: 2
  name: Hubspot Crm Feature Flags Paging Next Example
  slug: hubspot-crm-feature-flags-paging-next-example
- key_count: 2
  name: Hubspot Crm Feature Flags Portal Flag State Collection Example
  slug: hubspot-crm-feature-flags-portal-flag-state-collection-example
- key_count: 4
  name: Hubspot Crm Feature Flags Portal Flag State Example
  slug: hubspot-crm-feature-flags-portal-flag-state-example
- key_count: 1
  name: Hubspot Crm Feature Flags Portal Flag State Input Example
  slug: hubspot-crm-feature-flags-portal-flag-state-input-example
- key_count: 2
  name: Hubspot Crm Lists Collection Response List Example
  slug: hubspot-crm-lists-collection-response-list-example
- key_count: 2
  name: Hubspot Crm Lists Collection Response Membership Example
  slug: hubspot-crm-lists-collection-response-membership-example
- key_count: 4
  name: Hubspot Crm Lists Error Example
  slug: hubspot-crm-lists-error-example
- key_count: 4
  name: Hubspot Crm Lists List Create Request Example
  slug: hubspot-crm-lists-list-create-request-example
- key_count: 9
  name: Hubspot Crm Lists List Example
  slug: hubspot-crm-lists-list-example
- key_count: 2
  name: Hubspot Crm Lists Membership Change Request Example
  slug: hubspot-crm-lists-membership-change-request-example
- key_count: 4
  name: Hubspot Crm Lists Membership Change Response Example
  slug: hubspot-crm-lists-membership-change-response-example
- key_count: 2
  name: Hubspot Crm Lists Membership Example
  slug: hubspot-crm-lists-membership-example
- key_count: 1
  name: Hubspot Crm Lists Paging Example
  slug: hubspot-crm-lists-paging-example
- key_count: 5
  name: Hubspot Crm Search Crm Object Example
  slug: hubspot-crm-search-crm-object-example
- key_count: 5
  name: Hubspot Crm Search Error Example
  slug: hubspot-crm-search-error-example
- key_count: 5
  name: Hubspot Crm Search Filter Example
  slug: hubspot-crm-search-filter-example
- key_count: 1
  name: Hubspot Crm Search Filter Group Example
  slug: hubspot-crm-search-filter-group-example
- key_count: 1
  name: Hubspot Crm Search Paging Example
  slug: hubspot-crm-search-paging-example
- key_count: 6
  name: Hubspot Crm Search Search Request Example
  slug: hubspot-crm-search-search-request-example
- key_count: 3
  name: Hubspot Crm Search Search Response Example
  slug: hubspot-crm-search-search-response-example
- key_count: 2
  name: Hubspot Crm Search Sort Example
  slug: hubspot-crm-search-sort-example
- key_count: 2
  name: Hubspot Crm Tickets Association Example
  slug: hubspot-crm-tickets-association-example
- key_count: 1
  name: Hubspot Crm Tickets Batch Archive Input Example
  slug: hubspot-crm-tickets-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Tickets Batch Create Input Example
  slug: hubspot-crm-tickets-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Tickets Batch Read Input Example
  slug: hubspot-crm-tickets-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Tickets Batch Response Ticket Example
  slug: hubspot-crm-tickets-batch-response-ticket-example
- key_count: 1
  name: Hubspot Crm Tickets Batch Update Input Example
  slug: hubspot-crm-tickets-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Tickets Collection Response Association Example
  slug: hubspot-crm-tickets-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Tickets Collection Response Ticket Example
  slug: hubspot-crm-tickets-collection-response-ticket-example
- key_count: 4
  name: Hubspot Crm Tickets Error Example
  slug: hubspot-crm-tickets-error-example
- key_count: 3
  name: Hubspot Crm Tickets Filter Example
  slug: hubspot-crm-tickets-filter-example
- key_count: 1
  name: Hubspot Crm Tickets Filter Group Example
  slug: hubspot-crm-tickets-filter-group-example
- key_count: 1
  name: Hubspot Crm Tickets Paging Example
  slug: hubspot-crm-tickets-paging-example
- key_count: 6
  name: Hubspot Crm Tickets Search Request Example
  slug: hubspot-crm-tickets-search-request-example
- key_count: 1
  name: Hubspot Crm Tickets Simple Public Object Input Example
  slug: hubspot-crm-tickets-simple-public-object-input-example
- key_count: 6
  name: Hubspot Crm Tickets Ticket Example
  slug: hubspot-crm-tickets-ticket-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Action Definition Collection Example
  slug: hubspot-custom-workflow-actions-action-definition-collection-example
- key_count: 10
  name: Hubspot Custom Workflow Actions Action Definition Example
  slug: hubspot-custom-workflow-actions-action-definition-example
- key_count: 7
  name: Hubspot Custom Workflow Actions Action Definition Input Example
  slug: hubspot-custom-workflow-actions-action-definition-input-example
- key_count: 7
  name: Hubspot Custom Workflow Actions Action Definition Patch Example
  slug: hubspot-custom-workflow-actions-action-definition-patch-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Action Definition Revision Collection Example
  slug: hubspot-custom-workflow-actions-action-definition-revision-collection-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Action Definition Revision Example
  slug: hubspot-custom-workflow-actions-action-definition-revision-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Action Function Collection Example
  slug: hubspot-custom-workflow-actions-action-function-collection-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Action Function Example
  slug: hubspot-custom-workflow-actions-action-function-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Action Function Input Example
  slug: hubspot-custom-workflow-actions-action-function-input-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Action Function Reference Example
  slug: hubspot-custom-workflow-actions-action-function-reference-example
- key_count: 4
  name: Hubspot Custom Workflow Actions Action Labels Example
  slug: hubspot-custom-workflow-actions-action-labels-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Batch Callback Completion Request Example
  slug: hubspot-custom-workflow-actions-batch-callback-completion-request-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Batch Callback Error Example
  slug: hubspot-custom-workflow-actions-batch-callback-error-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Batch Callback Input Example
  slug: hubspot-custom-workflow-actions-batch-callback-input-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Batch Callback Response Example
  slug: hubspot-custom-workflow-actions-batch-callback-response-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Callback Completion Request Example
  slug: hubspot-custom-workflow-actions-callback-completion-request-example
- key_count: 5
  name: Hubspot Custom Workflow Actions Error Detail Example
  slug: hubspot-custom-workflow-actions-error-detail-example
- key_count: 7
  name: Hubspot Custom Workflow Actions Error Example
  slug: hubspot-custom-workflow-actions-error-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Field Option Example
  slug: hubspot-custom-workflow-actions-field-option-example
- key_count: 6
  name: Hubspot Custom Workflow Actions Field Type Definition Example
  slug: hubspot-custom-workflow-actions-field-type-definition-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Input Field Example
  slug: hubspot-custom-workflow-actions-input-field-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Object Request Options Example
  slug: hubspot-custom-workflow-actions-object-request-options-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Output Field Example
  slug: hubspot-custom-workflow-actions-output-field-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Paging Example
  slug: hubspot-custom-workflow-actions-paging-example
- key_count: 3
  name: Hubspot Domains Domain Collection Response Example
  slug: hubspot-domains-domain-collection-response-example
- key_count: 21
  name: Hubspot Domains Domain Example
  slug: hubspot-domains-domain-example
- key_count: 5
  name: Hubspot Domains Error Detail Example
  slug: hubspot-domains-error-detail-example
- key_count: 7
  name: Hubspot Domains Error Example
  slug: hubspot-domains-error-example
- key_count: 1
  name: Hubspot Domains Forward Paging Example
  slug: hubspot-domains-forward-paging-example
- key_count: 2
  name: Hubspot Domains Next Page Example
  slug: hubspot-domains-next-page-example
- key_count: 2
  name: Hubspot Engagement Calls Association Input Example
  slug: hubspot-engagement-calls-association-input-example
- key_count: 2
  name: Hubspot Engagement Calls Association Type Example
  slug: hubspot-engagement-calls-association-type-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Archive Calls Request Example
  slug: hubspot-engagement-calls-batch-archive-calls-request-example
- key_count: 7
  name: Hubspot Engagement Calls Batch Calls Response Example
  slug: hubspot-engagement-calls-batch-calls-response-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Create Calls Request Example
  slug: hubspot-engagement-calls-batch-create-calls-request-example
- key_count: 5
  name: Hubspot Engagement Calls Batch Error Example
  slug: hubspot-engagement-calls-batch-error-example
- key_count: 4
  name: Hubspot Engagement Calls Batch Read Calls Request Example
  slug: hubspot-engagement-calls-batch-read-calls-request-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Read Input Example
  slug: hubspot-engagement-calls-batch-read-input-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Update Calls Request Example
  slug: hubspot-engagement-calls-batch-update-calls-request-example
- key_count: 2
  name: Hubspot Engagement Calls Batch Update Input Example
  slug: hubspot-engagement-calls-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Calls Call Collection Response Example
  slug: hubspot-engagement-calls-call-collection-response-example
- key_count: 2
  name: Hubspot Engagement Calls Call Create Request Example
  slug: hubspot-engagement-calls-call-create-request-example
- key_count: 7
  name: Hubspot Engagement Calls Call Example
  slug: hubspot-engagement-calls-call-example
- key_count: 6
  name: Hubspot Engagement Calls Call Search Request Example
  slug: hubspot-engagement-calls-call-search-request-example
- key_count: 3
  name: Hubspot Engagement Calls Call Search Response Example
  slug: hubspot-engagement-calls-call-search-response-example
- key_count: 1
  name: Hubspot Engagement Calls Call Update Request Example
  slug: hubspot-engagement-calls-call-update-request-example
- key_count: 5
  name: Hubspot Engagement Calls Error Detail Example
  slug: hubspot-engagement-calls-error-detail-example
- key_count: 7
  name: Hubspot Engagement Calls Error Example
  slug: hubspot-engagement-calls-error-example
- key_count: 5
  name: Hubspot Engagement Calls Filter Example
  slug: hubspot-engagement-calls-filter-example
- key_count: 1
  name: Hubspot Engagement Calls Filter Group Example
  slug: hubspot-engagement-calls-filter-group-example
- key_count: 2
  name: Hubspot Engagement Calls Gdpr Delete Request Example
  slug: hubspot-engagement-calls-gdpr-delete-request-example
- key_count: 2
  name: Hubspot Engagement Calls Next Page Example
  slug: hubspot-engagement-calls-next-page-example
- key_count: 1
  name: Hubspot Engagement Calls Paging Example
  slug: hubspot-engagement-calls-paging-example
- key_count: 6
  name: Hubspot Engagement Calls Property History Example
  slug: hubspot-engagement-calls-property-history-example
- key_count: 2
  name: Hubspot Engagement Calls Sort Option Example
  slug: hubspot-engagement-calls-sort-option-example
- key_count: 2
  name: Hubspot Engagement Emails Association Example
  slug: hubspot-engagement-emails-association-example
- key_count: 1
  name: Hubspot Engagement Emails Batch Create Input Example
  slug: hubspot-engagement-emails-batch-create-input-example
- key_count: 2
  name: Hubspot Engagement Emails Batch Read Input Example
  slug: hubspot-engagement-emails-batch-read-input-example
- key_count: 1
  name: Hubspot Engagement Emails Batch Update Input Example
  slug: hubspot-engagement-emails-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Emails Collection Response Association Example
  slug: hubspot-engagement-emails-collection-response-association-example
- key_count: 4
  name: Hubspot Engagement Emails Error Example
  slug: hubspot-engagement-emails-error-example
- key_count: 3
  name: Hubspot Engagement Emails Filter Example
  slug: hubspot-engagement-emails-filter-example
- key_count: 1
  name: Hubspot Engagement Emails Filter Group Example
  slug: hubspot-engagement-emails-filter-group-example
- key_count: 1
  name: Hubspot Engagement Emails Paging Example
  slug: hubspot-engagement-emails-paging-example
- key_count: 6
  name: Hubspot Engagement Emails Search Request Example
  slug: hubspot-engagement-emails-search-request-example
- key_count: 1
  name: Hubspot Engagement Emails Simple Public Object Input Example
  slug: hubspot-engagement-emails-simple-public-object-input-example
- key_count: 2
  name: Hubspot Engagement Meetings Association Example
  slug: hubspot-engagement-meetings-association-example
- key_count: 1
  name: Hubspot Engagement Meetings Batch Create Input Example
  slug: hubspot-engagement-meetings-batch-create-input-example
- key_count: 2
  name: Hubspot Engagement Meetings Batch Read Input Example
  slug: hubspot-engagement-meetings-batch-read-input-example
- key_count: 3
  name: Hubspot Engagement Meetings Batch Response Meeting Example
  slug: hubspot-engagement-meetings-batch-response-meeting-example
- key_count: 1
  name: Hubspot Engagement Meetings Batch Update Input Example
  slug: hubspot-engagement-meetings-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Meetings Collection Response Association Example
  slug: hubspot-engagement-meetings-collection-response-association-example
- key_count: 2
  name: Hubspot Engagement Meetings Collection Response Meeting Example
  slug: hubspot-engagement-meetings-collection-response-meeting-example
- key_count: 4
  name: Hubspot Engagement Meetings Error Example
  slug: hubspot-engagement-meetings-error-example
- key_count: 3
  name: Hubspot Engagement Meetings Filter Example
  slug: hubspot-engagement-meetings-filter-example
- key_count: 1
  name: Hubspot Engagement Meetings Filter Group Example
  slug: hubspot-engagement-meetings-filter-group-example
- key_count: 6
  name: Hubspot Engagement Meetings Meeting Example
  slug: hubspot-engagement-meetings-meeting-example
- key_count: 1
  name: Hubspot Engagement Meetings Paging Example
  slug: hubspot-engagement-meetings-paging-example
- key_count: 6
  name: Hubspot Engagement Meetings Search Request Example
  slug: hubspot-engagement-meetings-search-request-example
- key_count: 1
  name: Hubspot Engagement Meetings Simple Public Object Input Example
  slug: hubspot-engagement-meetings-simple-public-object-input-example
- key_count: 2
  name: Hubspot Engagement Notes Association Input Example
  slug: hubspot-engagement-notes-association-input-example
- key_count: 2
  name: Hubspot Engagement Notes Association Type Example
  slug: hubspot-engagement-notes-association-type-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Archive Notes Request Example
  slug: hubspot-engagement-notes-batch-archive-notes-request-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Create Notes Request Example
  slug: hubspot-engagement-notes-batch-create-notes-request-example
- key_count: 5
  name: Hubspot Engagement Notes Batch Error Example
  slug: hubspot-engagement-notes-batch-error-example
- key_count: 7
  name: Hubspot Engagement Notes Batch Notes Response Example
  slug: hubspot-engagement-notes-batch-notes-response-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Read Input Example
  slug: hubspot-engagement-notes-batch-read-input-example
- key_count: 4
  name: Hubspot Engagement Notes Batch Read Notes Request Example
  slug: hubspot-engagement-notes-batch-read-notes-request-example
- key_count: 2
  name: Hubspot Engagement Notes Batch Update Input Example
  slug: hubspot-engagement-notes-batch-update-input-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Update Notes Request Example
  slug: hubspot-engagement-notes-batch-update-notes-request-example
- key_count: 5
  name: Hubspot Engagement Notes Error Detail Example
  slug: hubspot-engagement-notes-error-detail-example
- key_count: 7
  name: Hubspot Engagement Notes Error Example
  slug: hubspot-engagement-notes-error-example
- key_count: 5
  name: Hubspot Engagement Notes Filter Example
  slug: hubspot-engagement-notes-filter-example
- key_count: 1
  name: Hubspot Engagement Notes Filter Group Example
  slug: hubspot-engagement-notes-filter-group-example
- key_count: 2
  name: Hubspot Engagement Notes Gdpr Delete Request Example
  slug: hubspot-engagement-notes-gdpr-delete-request-example
- key_count: 2
  name: Hubspot Engagement Notes Next Page Example
  slug: hubspot-engagement-notes-next-page-example
- key_count: 2
  name: Hubspot Engagement Notes Note Collection Response Example
  slug: hubspot-engagement-notes-note-collection-response-example
- key_count: 2
  name: Hubspot Engagement Notes Note Create Request Example
  slug: hubspot-engagement-notes-note-create-request-example
- key_count: 7
  name: Hubspot Engagement Notes Note Example
  slug: hubspot-engagement-notes-note-example
- key_count: 6
  name: Hubspot Engagement Notes Note Search Request Example
  slug: hubspot-engagement-notes-note-search-request-example
- key_count: 3
  name: Hubspot Engagement Notes Note Search Response Example
  slug: hubspot-engagement-notes-note-search-response-example
- key_count: 1
  name: Hubspot Engagement Notes Note Update Request Example
  slug: hubspot-engagement-notes-note-update-request-example
- key_count: 1
  name: Hubspot Engagement Notes Paging Example
  slug: hubspot-engagement-notes-paging-example
- key_count: 6
  name: Hubspot Engagement Notes Property History Example
  slug: hubspot-engagement-notes-property-history-example
- key_count: 2
  name: Hubspot Engagement Notes Sort Option Example
  slug: hubspot-engagement-notes-sort-option-example
- key_count: 2
  name: Hubspot Engagement Tasks Association Example
  slug: hubspot-engagement-tasks-association-example
- key_count: 1
  name: Hubspot Engagement Tasks Batch Create Input Example
  slug: hubspot-engagement-tasks-batch-create-input-example
- key_count: 2
  name: Hubspot Engagement Tasks Batch Read Input Example
  slug: hubspot-engagement-tasks-batch-read-input-example
- key_count: 3
  name: Hubspot Engagement Tasks Batch Response Task Example
  slug: hubspot-engagement-tasks-batch-response-task-example
- key_count: 1
  name: Hubspot Engagement Tasks Batch Update Input Example
  slug: hubspot-engagement-tasks-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Tasks Collection Response Association Example
  slug: hubspot-engagement-tasks-collection-response-association-example
- key_count: 2
  name: Hubspot Engagement Tasks Collection Response Task Example
  slug: hubspot-engagement-tasks-collection-response-task-example
- key_count: 4
  name: Hubspot Engagement Tasks Error Example
  slug: hubspot-engagement-tasks-error-example
- key_count: 3
  name: Hubspot Engagement Tasks Filter Example
  slug: hubspot-engagement-tasks-filter-example
- key_count: 1
  name: Hubspot Engagement Tasks Filter Group Example
  slug: hubspot-engagement-tasks-filter-group-example
- key_count: 1
  name: Hubspot Engagement Tasks Paging Example
  slug: hubspot-engagement-tasks-paging-example
- key_count: 6
  name: Hubspot Engagement Tasks Search Request Example
  slug: hubspot-engagement-tasks-search-request-example
- key_count: 1
  name: Hubspot Engagement Tasks Simple Public Object Input Example
  slug: hubspot-engagement-tasks-simple-public-object-input-example
- key_count: 6
  name: Hubspot Engagement Tasks Task Example
  slug: hubspot-engagement-tasks-task-example
- key_count: 5
  name: Hubspot Marketing Emal Error Detail Example
  slug: hubspot-marketing-emal-error-detail-example
- key_count: 7
  name: Hubspot Marketing Emal Error Example
  slug: hubspot-marketing-emal-error-example
- key_count: 2
  name: Hubspot Marketing Emal Next Page Example
  slug: hubspot-marketing-emal-next-page-example
- key_count: 1
  name: Hubspot Marketing Emal Paging Example
  slug: hubspot-marketing-emal-paging-example
- key_count: 2
  name: Hubspot Marketing Emal Smtp Token Collection Response Example
  slug: hubspot-marketing-emal-smtp-token-collection-response-example
- key_count: 2
  name: Hubspot Marketing Emal Smtp Token Create Request Example
  slug: hubspot-marketing-emal-smtp-token-create-request-example
- key_count: 6
  name: Hubspot Marketing Emal Smtp Token Example
  slug: hubspot-marketing-emal-smtp-token-example
- key_count: 7
  name: Hubspot Marketing Emal Smtp Token With Password Example
  slug: hubspot-marketing-emal-smtp-token-with-password-example
- key_count: 9
  name: Hubspot Oauth Access Token Metadata Example
  slug: hubspot-oauth-access-token-metadata-example
- key_count: 5
  name: Hubspot Oauth Error Detail Example
  slug: hubspot-oauth-error-detail-example
- key_count: 7
  name: Hubspot Oauth Error Example
  slug: hubspot-oauth-error-example
- key_count: 6
  name: Hubspot Oauth Refresh Token Metadata Example
  slug: hubspot-oauth-refresh-token-metadata-example
- key_count: 6
  name: Hubspot Oauth Token Request Example
  slug: hubspot-oauth-token-request-example
- key_count: 5
  name: Hubspot Oauth Token Response Example
  slug: hubspot-oauth-token-response-example
- key_count: 5
  name: Hubspot Source Code Action Response Example
  slug: hubspot-source-code-action-response-example
- key_count: 8
  name: Hubspot Source Code Asset File Metadata Example
  slug: hubspot-source-code-asset-file-metadata-example
- key_count: 5
  name: Hubspot Source Code Error Detail Example
  slug: hubspot-source-code-error-detail-example
- key_count: 7
  name: Hubspot Source Code Error Example
  slug: hubspot-source-code-error-example
- key_count: 1
  name: Hubspot Source Code File Extract Request Example
  slug: hubspot-source-code-file-extract-request-example
- key_count: 1
  name: Hubspot Source Code File Upload Request Example
  slug: hubspot-source-code-file-upload-request-example
- key_count: 2
  name: Hubspot Source Code Task Locator Example
  slug: hubspot-source-code-task-locator-example
- key_count: 6
  name: Marketing Emal Api Email Message Example
  slug: marketing-emal-api-email-message-example
- key_count: 2
  name: Marketing Emal Api Next Page Example
  slug: marketing-emal-api-next-page-example
- key_count: 1
  name: Marketing Emal Api Paging Example
  slug: marketing-emal-api-paging-example
- key_count: 2
  name: Marketing Emal Api Smtp Token Collection Response Example
  slug: marketing-emal-api-smtp-token-collection-response-example
- key_count: 2
  name: Marketing Emal Api Smtp Token Create Request Example
  slug: marketing-emal-api-smtp-token-create-request-example
- key_count: 6
  name: Marketing Emal Api Smtp Token Example
  slug: marketing-emal-api-smtp-token-example
- key_count: 7
  name: Marketing Emal Api Smtp Token With Password Example
  slug: marketing-emal-api-smtp-token-with-password-example
- key_count: 4
  name: Marketing Emal Api Transactional Email Request Example
  slug: marketing-emal-api-transactional-email-request-example
- key_count: 6
  name: Marketing Emal Api Transactional Email Response Example
  slug: marketing-emal-api-transactional-email-response-example
- key_count: 9
  name: Oauth Api Access Token Metadata Example
  slug: oauth-api-access-token-metadata-example
- key_count: 6
  name: Oauth Api Refresh Token Metadata Example
  slug: oauth-api-refresh-token-metadata-example
- key_count: 6
  name: Oauth Api Token Request Example
  slug: oauth-api-token-request-example
- key_count: 5
  name: Oauth Api Token Response Example
  slug: oauth-api-token-response-example
- key_count: 5
  name: Source Code Api Action Response Example
  slug: source-code-api-action-response-example
- key_count: 8
  name: Source Code Api Asset File Metadata Example
  slug: source-code-api-asset-file-metadata-example
- key_count: 1
  name: Source Code Api File Extract Request Example
  slug: source-code-api-file-extract-request-example
- key_count: 1
  name: Source Code Api File Upload Request Example
  slug: source-code-api-file-upload-request-example
- key_count: 2
  name: Source Code Api Task Locator Example
  slug: source-code-api-task-locator-example
- key_count: 4
  name: Source Code Api Validation Error Example
  slug: source-code-api-validation-error-example
- key_count: 3
  name: Source Code Api Validation Result Example
  slug: source-code-api-validation-result-example
- key_count: 3
  name: Source Code Api Validation Warning Example
  slug: source-code-api-validation-warning-example
features:
- Free CRM with unlimited free users
- Marketing Hub Starter at $9/seat/mo annual
- Marketing Hub Professional at $890/mo with mandatory $3,000 onboarding
- Marketing Hub Enterprise at $3,600/mo with $7,000 onboarding
- Sales, Service, Operations, CMS, and Content Hubs with parallel tiering
- Marketing Contact-based pricing (1k included Starter, 2k Pro, 10k Enterprise)
- Additional 5,000 contacts at $250/month on Professional
- Additional seats at $45/month (Pro) or $75/month (Enterprise)
- REST API at 250k req/day Free/Starter, 500k Pro/Enterprise
- 100 req/10s burst (Free/Starter), 150 req/10s (Pro/Enterprise)
- Search API limited to 4 req/sec
- Batch endpoints up to 100 objects per request
- Custom objects on Enterprise
- Workflows, sequences, and automation
- OAuth 2.0 and private app tokens
- Webhooks v3 for object change events
finops:
- name: Hubspot Finops
  service_category: CRM and Marketing Automation
  slug: hubspot-finops
graphqls:
- description: HubSpot does not currently offer a public GraphQL API. All platform capabilities are exposed through a
  name: HubSpot GraphQL
  slug: hubspot-graphql
image: https://www.hubspot.com/hubfs/HubSpot_Logos/HubSpot-Inversed-Favicon.png
integrations:
- description: Bi-directional CRM sync between HubSpot and Salesforce for unified sales and marketing data.
  name: Salesforce
- description: Send HubSpot notifications, create tasks, and share CRM data directly in Slack channels.
  name: Slack
- description: Sync contacts, calendar events, and emails between HubSpot and Google Workspace apps.
  name: Google Workspace
- description: Connect Outlook email, calendar, and contacts with HubSpot CRM for seamless productivity.
  name: Microsoft 365
- description: Automatically log Zoom meeting details and recordings on CRM contact timelines.
  name: Zoom
- description: Sync ecommerce order data, products, and customers between Shopify and HubSpot.
  name: Shopify
- description: Embed HubSpot forms, live chat, and analytics on WordPress sites with the official plugin.
  name: WordPress
- description: Process payments and sync transaction data between Stripe and HubSpot Commerce.
  name: Stripe
- description: Connect HubSpot with thousands of apps through automated Zapier workflows.
  name: Zapier
- description: Sync support tickets and development issues between HubSpot and Jira.
  name: Jira
- description: Sync invoices, payments, and customer data between HubSpot and QuickBooks.
  name: QuickBooks
- description: Share HubSpot CRM and marketing data with Snowflake for advanced analytics.
  name: Snowflake
- description: Track ad performance and sync audiences between HubSpot and Google Ads.
  name: Google Ads
- description: Create and manage Facebook ad campaigns with HubSpot audience targeting.
  name: Facebook Ads
- description: Sync LinkedIn lead gen forms and ads data with HubSpot for B2B marketing.
  name: LinkedIn
json_schemas:
- name: EventInstanceCollection
  property_count: 2
  slug: analytics-events-api-event-instance-collection
- name: EventInstance
  property_count: 6
  slug: analytics-events-api-event-instance
- name: EventTypeCollection
  property_count: 1
  slug: analytics-events-api-event-type-collection
- name: PagingNext
  property_count: 2
  slug: analytics-events-api-paging-next
- name: PagingPrevious
  property_count: 2
  slug: analytics-events-api-paging-previous
- name: Paging
  property_count: 2
  slug: analytics-events-api-paging
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: authors-api-attach-to-language-group-request
- name: BatchArchiveInput
  property_count: 1
  slug: authors-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: authors-api-batch-create-input
- name: BatchInputItem
  property_count: 2
  slug: authors-api-batch-input-item
- name: BatchInput
  property_count: 1
  slug: authors-api-batch-input
- name: BatchReadInput
  property_count: 1
  slug: authors-api-batch-read-input
- name: BatchResponse
  property_count: 6
  slug: authors-api-batch-response
- name: BatchResponseWithErrors
  property_count: 0
  slug: authors-api-batch-response-with-errors
- name: BlogAuthorCollection
  property_count: 3
  slug: authors-api-blog-author-collection
- name: BlogAuthorInput
  property_count: 9
  slug: authors-api-blog-author-input
- name: BlogAuthor
  property_count: 15
  slug: authors-api-blog-author
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: authors-api-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: authors-api-detach-from-language-group-request
- name: PagingNext
  property_count: 2
  slug: authors-api-paging-next
- name: Paging
  property_count: 1
  slug: authors-api-paging
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: authors-api-set-language-primary-request
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: blog-posts-api-attach-to-language-group-request
- name: BatchInputItem
  property_count: 1
  slug: blog-posts-api-batch-input-item
- name: BatchInput
  property_count: 1
  slug: blog-posts-api-batch-input
- name: BatchResponse
  property_count: 6
  slug: blog-posts-api-batch-response
- name: BatchResponseWithErrors
  property_count: 0
  slug: blog-posts-api-batch-response-with-errors
- name: BlogPostCollection
  property_count: 3
  slug: blog-posts-api-blog-post-collection
- name: BlogPostInput
  property_count: 15
  slug: blog-posts-api-blog-post-input
- name: BlogPost
  property_count: 32
  slug: blog-posts-api-blog-post
- name: CloneRequest
  property_count: 1
  slug: blog-posts-api-clone-request
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: blog-posts-api-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: blog-posts-api-detach-from-language-group-request
- name: PagingNext
  property_count: 2
  slug: blog-posts-api-paging-next
- name: PagingPrevious
  property_count: 2
  slug: blog-posts-api-paging-previous
- name: Paging
  property_count: 2
  slug: blog-posts-api-paging
- name: PushLiveRequest
  property_count: 1
  slug: blog-posts-api-push-live-request
- name: ResetDraftRequest
  property_count: 1
  slug: blog-posts-api-reset-draft-request
- name: RestorePreviousVersionRequest
  property_count: 2
  slug: blog-posts-api-restore-previous-version-request
- name: ScheduleRequest
  property_count: 2
  slug: blog-posts-api-schedule-request
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: blog-posts-api-set-language-primary-request
- name: VersionHistory
  property_count: 4
  slug: blog-posts-api-version-history
- name: CollectionResponseHubDBRow
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbrow
- name: CollectionResponseHubDBTable
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbtable
- name: HubDBColumn
  property_count: 5
  slug: cms-hubdb-api-hub-dbcolumn
- name: HubDBRowCreateRequest
  property_count: 1
  slug: cms-hubdb-api-hub-dbrow-create-request
- name: HubDBRow
  property_count: 4
  slug: cms-hubdb-api-hub-dbrow
- name: HubDBTableCreateRequest
  property_count: 3
  slug: cms-hubdb-api-hub-dbtable-create-request
- name: HubDBTable
  property_count: 9
  slug: cms-hubdb-api-hub-dbtable
- name: Paging
  property_count: 1
  slug: cms-hubdb-api-paging
- name: CollectionResponsePage
  property_count: 2
  slug: cms-pages-api-collection-response-page
- name: PageCreateRequest
  property_count: 8
  slug: cms-pages-api-page-create-request
- name: Page
  property_count: 16
  slug: cms-pages-api-page
- name: PageUpdateRequest
  property_count: 5
  slug: cms-pages-api-page-update-request
- name: Paging
  property_count: 1
  slug: cms-pages-api-paging
- name: AssociationInput
  property_count: 2
  slug: commerce-payments-api-association-input
- name: AssociationResult
  property_count: 2
  slug: commerce-payments-api-association-result
- name: AssociationType
  property_count: 2
  slug: commerce-payments-api-association-type
- name: BatchArchiveRequest
  property_count: 1
  slug: commerce-payments-api-batch-archive-request
- name: BatchCreateRequest
  property_count: 1
  slug: commerce-payments-api-batch-create-request
- name: BatchCreateResponse
  property_count: 8
  slug: commerce-payments-api-batch-create-response
- name: BatchError
  property_count: 8
  slug: commerce-payments-api-batch-error
- name: BatchReadInputItem
  property_count: 1
  slug: commerce-payments-api-batch-read-input-item
- name: BatchReadRequest
  property_count: 4
  slug: commerce-payments-api-batch-read-request
- name: BatchReadResponse
  property_count: 8
  slug: commerce-payments-api-batch-read-response
- name: BatchUpdateInputItem
  property_count: 3
  slug: commerce-payments-api-batch-update-input-item
- name: BatchUpdateRequest
  property_count: 1
  slug: commerce-payments-api-batch-update-request
- name: BatchUpdateResponse
  property_count: 8
  slug: commerce-payments-api-batch-update-response
- name: CommercePaymentCollection
  property_count: 2
  slug: commerce-payments-api-commerce-payment-collection
- name: CommercePaymentInput
  property_count: 2
  slug: commerce-payments-api-commerce-payment-input
- name: CommercePaymentPatch
  property_count: 1
  slug: commerce-payments-api-commerce-payment-patch
- name: CommercePayment
  property_count: 8
  slug: commerce-payments-api-commerce-payment
- name: FilterGroup
  property_count: 1
  slug: commerce-payments-api-filter-group
- name: Filter
  property_count: 5
  slug: commerce-payments-api-filter
- name: Paging
  property_count: 2
  slug: commerce-payments-api-paging
- name: PropertyHistory
  property_count: 6
  slug: commerce-payments-api-property-history
- name: SearchRequest
  property_count: 6
  slug: commerce-payments-api-search-request
- name: SearchResponse
  property_count: 3
  slug: commerce-payments-api-search-response
- name: SortOption
  property_count: 2
  slug: commerce-payments-api-sort-option
- name: Association
  property_count: 2
  slug: commerce-subscriptions-api-association
- name: BatchCreateInput
  property_count: 1
  slug: commerce-subscriptions-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: commerce-subscriptions-api-batch-read-input
- name: BatchResponseSubscription
  property_count: 3
  slug: commerce-subscriptions-api-batch-response-subscription
- name: BatchUpdateInput
  property_count: 1
  slug: commerce-subscriptions-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-association
- name: CollectionResponseSubscription
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-subscription
- name: FilterGroup
  property_count: 1
  slug: commerce-subscriptions-api-filter-group
- name: Filter
  property_count: 3
  slug: commerce-subscriptions-api-filter
- name: Paging
  property_count: 1
  slug: commerce-subscriptions-api-paging
- name: SearchRequest
  property_count: 6
  slug: commerce-subscriptions-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: commerce-subscriptions-api-simple-public-object-input
- name: Subscription
  property_count: 6
  slug: commerce-subscriptions-api-subscription
- name: ActorCollection
  property_count: 2
  slug: conversations-api-actor-collection
- name: Actor
  property_count: 5
  slug: conversations-api-actor
- name: Attachment
  property_count: 5
  slug: conversations-api-attachment
- name: ChannelCollection
  property_count: 2
  slug: conversations-api-channel-collection
- name: Channel
  property_count: 5
  slug: conversations-api-channel
- name: InboxCollection
  property_count: 3
  slug: conversations-api-inbox-collection
- name: Inbox
  property_count: 6
  slug: conversations-api-inbox
- name: MessageCollection
  property_count: 2
  slug: conversations-api-message-collection
- name: MessageRecipient
  property_count: 1
  slug: conversations-api-message-recipient
- name: Message
  property_count: 13
  slug: conversations-api-message
- name: MessageStatus
  property_count: 1
  slug: conversations-api-message-status
- name: PagingNext
  property_count: 2
  slug: conversations-api-paging-next
- name: Paging
  property_count: 1
  slug: conversations-api-paging
- name: SendMessageRequest
  property_count: 7
  slug: conversations-api-send-message-request
- name: ThreadCollection
  property_count: 2
  slug: conversations-api-thread-collection
- name: Thread
  property_count: 14
  slug: conversations-api-thread
- name: UpdateThreadRequest
  property_count: 2
  slug: conversations-api-update-thread-request
- name: AssociationDefinitionCollection
  property_count: 2
  slug: crm-associations-api-association-definition-collection
- name: AssociationDefinition
  property_count: 7
  slug: crm-associations-api-association-definition
- name: AssociationLabelCollection
  property_count: 2
  slug: crm-associations-api-association-label-collection
- name: AssociationLabel
  property_count: 3
  slug: crm-associations-api-association-label
- name: AssociationResult
  property_count: 3
  slug: crm-associations-api-association-result
- name: Association
  property_count: 2
  slug: crm-associations-api-association
- name: AssociationTypeInput
  property_count: 2
  slug: crm-associations-api-association-type-input
- name: AssociationType
  property_count: 3
  slug: crm-associations-api-association-type
- name: BatchAssociationArchiveInput
  property_count: 1
  slug: crm-associations-api-batch-association-archive-input
- name: BatchAssociationArchiveItem
  property_count: 3
  slug: crm-associations-api-batch-association-archive-item
- name: BatchAssociationCreateInput
  property_count: 1
  slug: crm-associations-api-batch-association-create-input
- name: BatchAssociationCreateItem
  property_count: 3
  slug: crm-associations-api-batch-association-create-item
- name: BatchAssociationReadInput
  property_count: 1
  slug: crm-associations-api-batch-association-read-input
- name: BatchAssociationResponse
  property_count: 8
  slug: crm-associations-api-batch-association-response
- name: CreateAssociationInput
  property_count: 2
  slug: crm-associations-api-create-association-input
- name: CreateLabelInput
  property_count: 3
  slug: crm-associations-api-create-label-input
- name: ObjectReference
  property_count: 1
  slug: crm-associations-api-object-reference
- name: PagingNext
  property_count: 2
  slug: crm-associations-api-paging-next
- name: Paging
  property_count: 1
  slug: crm-associations-api-paging
- name: Association
  property_count: 2
  slug: crm-companies-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-companies-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-companies-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-companies-api-batch-read-input
- name: BatchResponseCompany
  property_count: 3
  slug: crm-companies-api-batch-response-company
- name: BatchUpdateInput
  property_count: 1
  slug: crm-companies-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-companies-api-collection-response-association
- name: CollectionResponseCompany
  property_count: 2
  slug: crm-companies-api-collection-response-company
- name: Company
  property_count: 6
  slug: crm-companies-api-company
- name: FilterGroup
  property_count: 1
  slug: crm-companies-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-companies-api-filter
- name: Paging
  property_count: 1
  slug: crm-companies-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-companies-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-companies-api-simple-public-object-input
- name: Association
  property_count: 2
  slug: crm-contacts-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-contacts-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-contacts-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-contacts-api-batch-read-input
- name: BatchResponseContact
  property_count: 3
  slug: crm-contacts-api-batch-response-contact
- name: BatchUpdateInput
  property_count: 1
  slug: crm-contacts-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-contacts-api-collection-response-association
- name: CollectionResponseContact
  property_count: 2
  slug: crm-contacts-api-collection-response-contact
- name: Contact
  property_count: 6
  slug: crm-contacts-api-contact
- name: FilterGroup
  property_count: 1
  slug: crm-contacts-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-contacts-api-filter
- name: Paging
  property_count: 1
  slug: crm-contacts-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-contacts-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-contacts-api-simple-public-object-input
- name: Association
  property_count: 2
  slug: crm-deals-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-deals-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-deals-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-deals-api-batch-read-input
- name: BatchResponseDeal
  property_count: 3
  slug: crm-deals-api-batch-response-deal
- name: BatchUpdateInput
  property_count: 1
  slug: crm-deals-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-deals-api-collection-response-association
- name: CollectionResponseDeal
  property_count: 2
  slug: crm-deals-api-collection-response-deal
- name: Deal
  property_count: 6
  slug: crm-deals-api-deal
- name: FilterGroup
  property_count: 1
  slug: crm-deals-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-deals-api-filter
- name: Paging
  property_count: 1
  slug: crm-deals-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-deals-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-deals-api-simple-public-object-input
- name: BatchDeleteInputItem
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input-item
- name: BatchDeleteInput
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input
- name: BatchError
  property_count: 4
  slug: crm-feature-flags-api-batch-error
- name: BatchPortalFlagStateInputItem
  property_count: 2
  slug: crm-feature-flags-api-batch-portal-flag-state-input-item
- name: BatchPortalFlagStateInput
  property_count: 1
  slug: crm-feature-flags-api-batch-portal-flag-state-input
- name: BatchPortalFlagStateResponse
  property_count: 4
  slug: crm-feature-flags-api-batch-portal-flag-state-response
- name: BatchPortalFlagStateResponseWithErrors
  property_count: 5
  slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors
- name: FeatureFlagInput
  property_count: 1
  slug: crm-feature-flags-api-feature-flag-input
- name: FeatureFlag
  property_count: 4
  slug: crm-feature-flags-api-feature-flag
- name: FlagState
  property_count: 0
  slug: crm-feature-flags-api-flag-state
- name: PagingNext
  property_count: 2
  slug: crm-feature-flags-api-paging-next
- name: Paging
  property_count: 1
  slug: crm-feature-flags-api-paging
- name: PortalFlagStateCollection
  property_count: 2
  slug: crm-feature-flags-api-portal-flag-state-collection
- name: PortalFlagStateInput
  property_count: 1
  slug: crm-feature-flags-api-portal-flag-state-input
- name: PortalFlagState
  property_count: 4
  slug: crm-feature-flags-api-portal-flag-state
- name: CollectionResponseList
  property_count: 2
  slug: crm-lists-api-collection-response-list
- name: CollectionResponseMembership
  property_count: 2
  slug: crm-lists-api-collection-response-membership
- name: ListCreateRequest
  property_count: 4
  slug: crm-lists-api-list-create-request
- name: List
  property_count: 9
  slug: crm-lists-api-list
- name: MembershipChangeRequest
  property_count: 2
  slug: crm-lists-api-membership-change-request
- name: MembershipChangeResponse
  property_count: 4
  slug: crm-lists-api-membership-change-response
- name: Membership
  property_count: 2
  slug: crm-lists-api-membership
- name: Paging
  property_count: 1
  slug: crm-lists-api-paging
- name: CRMObject
  property_count: 5
  slug: crm-search-api-crmobject
- name: FilterGroup
  property_count: 1
  slug: crm-search-api-filter-group
- name: Filter
  property_count: 5
  slug: crm-search-api-filter
- name: Paging
  property_count: 1
  slug: crm-search-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-search-api-search-request
- name: SearchResponse
  property_count: 3
  slug: crm-search-api-search-response
- name: Sort
  property_count: 2
  slug: crm-search-api-sort
- name: Association
  property_count: 2
  slug: crm-tickets-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-tickets-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-tickets-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-tickets-api-batch-read-input
- name: BatchResponseTicket
  property_count: 3
  slug: crm-tickets-api-batch-response-ticket
- name: BatchUpdateInput
  property_count: 1
  slug: crm-tickets-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-tickets-api-collection-response-association
- name: CollectionResponseTicket
  property_count: 2
  slug: crm-tickets-api-collection-response-ticket
- name: FilterGroup
  property_count: 1
  slug: crm-tickets-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-tickets-api-filter
- name: Paging
  property_count: 1
  slug: crm-tickets-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-tickets-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-tickets-api-simple-public-object-input
- name: Ticket
  property_count: 6
  slug: crm-tickets-api-ticket
- name: ActionDefinitionCollection
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-collection
- name: ActionDefinitionInput
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-input
- name: ActionDefinitionPatch
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-patch
- name: ActionDefinitionRevisionCollection
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-revision-collection
- name: ActionDefinitionRevision
  property_count: 3
  slug: custom-workflow-actions-api-action-definition-revision
- name: ActionDefinition
  property_count: 10
  slug: custom-workflow-actions-api-action-definition
- name: ActionFunctionCollection
  property_count: 1
  slug: custom-workflow-actions-api-action-function-collection
- name: ActionFunctionInput
  property_count: 1
  slug: custom-workflow-actions-api-action-function-input
- name: ActionFunctionReference
  property_count: 2
  slug: custom-workflow-actions-api-action-function-reference
- name: ActionFunction
  property_count: 3
  slug: custom-workflow-actions-api-action-function
- name: ActionLabels
  property_count: 4
  slug: custom-workflow-actions-api-action-labels
- name: BatchCallbackCompletionRequest
  property_count: 1
  slug: custom-workflow-actions-api-batch-callback-completion-request
- name: BatchCallbackError
  property_count: 3
  slug: custom-workflow-actions-api-batch-callback-error
- name: BatchCallbackInput
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-input
- name: BatchCallbackResponse
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-response
- name: CallbackCompletionRequest
  property_count: 1
  slug: custom-workflow-actions-api-callback-completion-request
- name: FieldOption
  property_count: 3
  slug: custom-workflow-actions-api-field-option
- name: FieldTypeDefinition
  property_count: 6
  slug: custom-workflow-actions-api-field-type-definition
- name: InputField
  property_count: 3
  slug: custom-workflow-actions-api-input-field
- name: ObjectRequestOptions
  property_count: 1
  slug: custom-workflow-actions-api-object-request-options
- name: OutputField
  property_count: 1
  slug: custom-workflow-actions-api-output-field
- name: Paging
  property_count: 1
  slug: custom-workflow-actions-api-paging
- name: DomainCollectionResponse
  property_count: 3
  slug: domains-api-domain-collection-response
- name: Domain
  property_count: 21
  slug: domains-api-domain
- name: ForwardPaging
  property_count: 1
  slug: domains-api-forward-paging
- name: NextPage
  property_count: 2
  slug: domains-api-next-page
- name: AssociationInput
  property_count: 2
  slug: engagement-calls-api-association-input
- name: AssociationType
  property_count: 2
  slug: engagement-calls-api-association-type
- name: BatchArchiveCallsRequest
  property_count: 1
  slug: engagement-calls-api-batch-archive-calls-request
- name: BatchCallsResponse
  property_count: 7
  slug: engagement-calls-api-batch-calls-response
- name: BatchCreateCallsRequest
  property_count: 1
  slug: engagement-calls-api-batch-create-calls-request
- name: BatchError
  property_count: 5
  slug: engagement-calls-api-batch-error
- name: BatchReadCallsRequest
  property_count: 4
  slug: engagement-calls-api-batch-read-calls-request
- name: BatchReadInput
  property_count: 1
  slug: engagement-calls-api-batch-read-input
- name: BatchUpdateCallsRequest
  property_count: 1
  slug: engagement-calls-api-batch-update-calls-request
- name: BatchUpdateInput
  property_count: 2
  slug: engagement-calls-api-batch-update-input
- name: CallCollectionResponse
  property_count: 2
  slug: engagement-calls-api-call-collection-response
- name: CallCreateRequest
  property_count: 2
  slug: engagement-calls-api-call-create-request
- name: Call
  property_count: 7
  slug: engagement-calls-api-call
- name: CallSearchRequest
  property_count: 6
  slug: engagement-calls-api-call-search-request
- name: CallSearchResponse
  property_count: 3
  slug: engagement-calls-api-call-search-response
- name: CallUpdateRequest
  property_count: 1
  slug: engagement-calls-api-call-update-request
- name: FilterGroup
  property_count: 1
  slug: engagement-calls-api-filter-group
- name: Filter
  property_count: 5
  slug: engagement-calls-api-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: engagement-calls-api-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: engagement-calls-api-next-page
- name: Paging
  property_count: 1
  slug: engagement-calls-api-paging
- name: PropertyHistory
  property_count: 6
  slug: engagement-calls-api-property-history
- name: SortOption
  property_count: 2
  slug: engagement-calls-api-sort-option
- name: Association
  property_count: 2
  slug: engagement-emails-api-association
- name: BatchCreateInput
  property_count: 1
  slug: engagement-emails-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: engagement-emails-api-batch-read-input
- name: BatchResponseEmailEngagement
  property_count: 3
  slug: engagement-emails-api-batch-response-email-engagement
- name: BatchUpdateInput
  property_count: 1
  slug: engagement-emails-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: engagement-emails-api-collection-response-association
- name: CollectionResponseEmailEngagement
  property_count: 2
  slug: engagement-emails-api-collection-response-email-engagement
- name: EmailEngagement
  property_count: 6
  slug: engagement-emails-api-email-engagement
- name: FilterGroup
  property_count: 1
  slug: engagement-emails-api-filter-group
- name: Filter
  property_count: 3
  slug: engagement-emails-api-filter
- name: Paging
  property_count: 1
  slug: engagement-emails-api-paging
- name: SearchRequest
  property_count: 6
  slug: engagement-emails-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: engagement-emails-api-simple-public-object-input
- name: Association
  property_count: 2
  slug: engagement-meetings-api-association
- name: BatchCreateInput
  property_count: 1
  slug: engagement-meetings-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: engagement-meetings-api-batch-read-input
- name: BatchResponseMeeting
  property_count: 3
  slug: engagement-meetings-api-batch-response-meeting
- name: BatchUpdateInput
  property_count: 1
  slug: engagement-meetings-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: engagement-meetings-api-collection-response-association
- name: CollectionResponseMeeting
  property_count: 2
  slug: engagement-meetings-api-collection-response-meeting
- name: FilterGroup
  property_count: 1
  slug: engagement-meetings-api-filter-group
- name: Filter
  property_count: 3
  slug: engagement-meetings-api-filter
- name: Meeting
  property_count: 6
  slug: engagement-meetings-api-meeting
- name: Paging
  property_count: 1
  slug: engagement-meetings-api-paging
- name: SearchRequest
  property_count: 6
  slug: engagement-meetings-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: engagement-meetings-api-simple-public-object-input
- name: AssociationInput
  property_count: 2
  slug: engagement-notes-association-input
- name: AssociationType
  property_count: 2
  slug: engagement-notes-association-type
- name: BatchArchiveNotesRequest
  property_count: 1
  slug: engagement-notes-batch-archive-notes-request
- name: BatchCreateNotesRequest
  property_count: 1
  slug: engagement-notes-batch-create-notes-request
- name: BatchError
  property_count: 5
  slug: engagement-notes-batch-error
- name: BatchNotesResponse
  property_count: 7
  slug: engagement-notes-batch-notes-response
- name: BatchReadInput
  property_count: 1
  slug: engagement-notes-batch-read-input
- name: BatchReadNotesRequest
  property_count: 4
  slug: engagement-notes-batch-read-notes-request
- name: BatchUpdateInput
  property_count: 2
  slug: engagement-notes-batch-update-input
- name: BatchUpdateNotesRequest
  property_count: 1
  slug: engagement-notes-batch-update-notes-request
- name: FilterGroup
  property_count: 1
  slug: engagement-notes-filter-group
- name: Filter
  property_count: 5
  slug: engagement-notes-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: engagement-notes-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: engagement-notes-next-page
- name: NoteCollectionResponse
  property_count: 2
  slug: engagement-notes-note-collection-response
- name: NoteCreateRequest
  property_count: 2
  slug: engagement-notes-note-create-request
- name: Note
  property_count: 7
  slug: engagement-notes-note
- name: NoteSearchRequest
  property_count: 6
  slug: engagement-notes-note-search-request
- name: NoteSearchResponse
  property_count: 3
  slug: engagement-notes-note-search-response
- name: NoteUpdateRequest
  property_count: 1
  slug: engagement-notes-note-update-request
- name: Paging
  property_count: 1
  slug: engagement-notes-paging
- name: PropertyHistory
  property_count: 6
  slug: engagement-notes-property-history
- name: SortOption
  property_count: 2
  slug: engagement-notes-sort-option
- name: Association
  property_count: 2
  slug: engagement-tasks-api-association
- name: BatchCreateInput
  property_count: 1
  slug: engagement-tasks-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: engagement-tasks-api-batch-read-input
- name: BatchResponseTask
  property_count: 3
  slug: engagement-tasks-api-batch-response-task
- name: BatchUpdateInput
  property_count: 1
  slug: engagement-tasks-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: engagement-tasks-api-collection-response-association
- name: CollectionResponseTask
  property_count: 2
  slug: engagement-tasks-api-collection-response-task
- name: FilterGroup
  property_count: 1
  slug: engagement-tasks-api-filter-group
- name: Filter
  property_count: 3
  slug: engagement-tasks-api-filter
- name: Paging
  property_count: 1
  slug: engagement-tasks-api-paging
- name: SearchRequest
  property_count: 6
  slug: engagement-tasks-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: engagement-tasks-api-simple-public-object-input
- name: Task
  property_count: 6
  slug: engagement-tasks-api-task
- name: ErrorDetail
  property_count: 5
  slug: hubspot-analytics-events-error-detail
- name: Error
  property_count: 7
  slug: hubspot-analytics-events-error
- name: EventInstanceCollection
  property_count: 2
  slug: hubspot-analytics-events-event-instance-collection
- name: EventInstance
  property_count: 6
  slug: hubspot-analytics-events-event-instance
- name: EventTypeCollection
  property_count: 1
  slug: hubspot-analytics-events-event-type-collection
- name: PagingNext
  property_count: 2
  slug: hubspot-analytics-events-paging-next
- name: PagingPrevious
  property_count: 2
  slug: hubspot-analytics-events-paging-previous
- name: Paging
  property_count: 2
  slug: hubspot-analytics-events-paging
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: hubspot-authors-attach-to-language-group-request
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-authors-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-authors-batch-create-input
- name: BatchInputItem
  property_count: 2
  slug: hubspot-authors-batch-input-item
- name: BatchInput
  property_count: 1
  slug: hubspot-authors-batch-input
- name: BatchReadInput
  property_count: 1
  slug: hubspot-authors-batch-read-input
- name: BatchResponse
  property_count: 6
  slug: hubspot-authors-batch-response
- name: BatchResponseWithErrors
  property_count: 0
  slug: hubspot-authors-batch-response-with-errors
- name: BlogAuthorCollection
  property_count: 3
  slug: hubspot-authors-blog-author-collection
- name: BlogAuthorInput
  property_count: 9
  slug: hubspot-authors-blog-author-input
- name: BlogAuthor
  property_count: 15
  slug: hubspot-authors-blog-author
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: hubspot-authors-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: hubspot-authors-detach-from-language-group-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-authors-error-detail
- name: Error
  property_count: 7
  slug: hubspot-authors-error
- name: PagingNext
  property_count: 2
  slug: hubspot-authors-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-authors-paging
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: hubspot-authors-set-language-primary-request
- name: StandardError
  property_count: 7
  slug: hubspot-authors-standard-error
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: hubspot-blog-posts-attach-to-language-group-request
- name: BatchInputItem
  property_count: 1
  slug: hubspot-blog-posts-batch-input-item
- name: BatchInput
  property_count: 1
  slug: hubspot-blog-posts-batch-input
- name: BatchResponse
  property_count: 6
  slug: hubspot-blog-posts-batch-response
- name: BatchResponseWithErrors
  property_count: 0
  slug: hubspot-blog-posts-batch-response-with-errors
- name: BlogPostCollection
  property_count: 3
  slug: hubspot-blog-posts-blog-post-collection
- name: BlogPostInput
  property_count: 15
  slug: hubspot-blog-posts-blog-post-input
- name: BlogPost
  property_count: 32
  slug: hubspot-blog-posts-blog-post
- name: CloneRequest
  property_count: 1
  slug: hubspot-blog-posts-clone-request
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: hubspot-blog-posts-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: hubspot-blog-posts-detach-from-language-group-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-blog-posts-error-detail
- name: Error
  property_count: 7
  slug: hubspot-blog-posts-error
- name: PagingNext
  property_count: 2
  slug: hubspot-blog-posts-paging-next
- name: PagingPrevious
  property_count: 2
  slug: hubspot-blog-posts-paging-previous
- name: Paging
  property_count: 2
  slug: hubspot-blog-posts-paging
- name: PushLiveRequest
  property_count: 1
  slug: hubspot-blog-posts-push-live-request
- name: ResetDraftRequest
  property_count: 1
  slug: hubspot-blog-posts-reset-draft-request
- name: RestorePreviousVersionRequest
  property_count: 2
  slug: hubspot-blog-posts-restore-previous-version-request
- name: ScheduleRequest
  property_count: 2
  slug: hubspot-blog-posts-schedule-request
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: hubspot-blog-posts-set-language-primary-request
- name: StandardError
  property_count: 7
  slug: hubspot-blog-posts-standard-error
- name: VersionHistory
  property_count: 4
  slug: hubspot-blog-posts-version-history
- name: CollectionResponseHubDBRow
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-row
- name: CollectionResponseHubDBTable
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-table
- name: Error
  property_count: 4
  slug: hubspot-cms-hubdb-error
- name: HubDBColumn
  property_count: 5
  slug: hubspot-cms-hubdb-hub-db-column
- name: HubDBRowCreateRequest
  property_count: 1
  slug: hubspot-cms-hubdb-hub-db-row-create-request
- name: HubDBRow
  property_count: 4
  slug: hubspot-cms-hubdb-hub-db-row
- name: HubDBTableCreateRequest
  property_count: 3
  slug: hubspot-cms-hubdb-hub-db-table-create-request
- name: HubDBTable
  property_count: 9
  slug: hubspot-cms-hubdb-hub-db-table
- name: Paging
  property_count: 1
  slug: hubspot-cms-hubdb-paging
- name: CollectionResponsePage
  property_count: 2
  slug: hubspot-cms-pages-collection-response-page
- name: Error
  property_count: 4
  slug: hubspot-cms-pages-error
- name: PageCreateRequest
  property_count: 8
  slug: hubspot-cms-pages-page-create-request
- name: Page
  property_count: 16
  slug: hubspot-cms-pages-page
- name: PageUpdateRequest
  property_count: 5
  slug: hubspot-cms-pages-page-update-request
- name: Paging
  property_count: 1
  slug: hubspot-cms-pages-paging
- name: AssociationInput
  property_count: 2
  slug: hubspot-commerce-payments-association-input
- name: AssociationResult
  property_count: 2
  slug: hubspot-commerce-payments-association-result
- name: AssociationType
  property_count: 2
  slug: hubspot-commerce-payments-association-type
- name: BatchArchiveRequest
  property_count: 1
  slug: hubspot-commerce-payments-batch-archive-request
- name: BatchCreateRequest
  property_count: 1
  slug: hubspot-commerce-payments-batch-create-request
- name: BatchCreateResponse
  property_count: 8
  slug: hubspot-commerce-payments-batch-create-response
- name: BatchError
  property_count: 8
  slug: hubspot-commerce-payments-batch-error
- name: BatchReadInputItem
  property_count: 1
  slug: hubspot-commerce-payments-batch-read-input-item
- name: BatchReadRequest
  property_count: 4
  slug: hubspot-commerce-payments-batch-read-request
- name: BatchReadResponse
  property_count: 8
  slug: hubspot-commerce-payments-batch-read-response
- name: BatchUpdateInputItem
  property_count: 3
  slug: hubspot-commerce-payments-batch-update-input-item
- name: BatchUpdateRequest
  property_count: 1
  slug: hubspot-commerce-payments-batch-update-request
- name: BatchUpdateResponse
  property_count: 8
  slug: hubspot-commerce-payments-batch-update-response
- name: CommercePaymentCollection
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-collection
- name: CommercePaymentInput
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-input
- name: CommercePaymentPatch
  property_count: 1
  slug: hubspot-commerce-payments-commerce-payment-patch
- name: CommercePayment
  property_count: 8
  slug: hubspot-commerce-payments-commerce-payment
- name: ErrorDetail
  property_count: 5
  slug: hubspot-commerce-payments-error-detail
- name: Error
  property_count: 7
  slug: hubspot-commerce-payments-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-commerce-payments-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-commerce-payments-filter
- name: Paging
  property_count: 2
  slug: hubspot-commerce-payments-paging
- name: PropertyHistory
  property_count: 6
  slug: hubspot-commerce-payments-property-history
- name: SearchRequest
  property_count: 6
  slug: hubspot-commerce-payments-search-request
- name: SearchResponse
  property_count: 3
  slug: hubspot-commerce-payments-search-response
- name: SortOption
  property_count: 2
  slug: hubspot-commerce-payments-sort-option
- name: Association
  property_count: 2
  slug: hubspot-commerce-subscriptions-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-commerce-subscriptions-batch-read-input
- name: BatchResponseSubscription
  property_count: 3
  slug: hubspot-commerce-subscriptions-batch-response-subscription
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-association
- name: CollectionResponseSubscription
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-subscription
- name: Error
  property_count: 4
  slug: hubspot-commerce-subscriptions-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-commerce-subscriptions-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-commerce-subscriptions-filter
- name: Paging
  property_count: 1
  slug: hubspot-commerce-subscriptions-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-commerce-subscriptions-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-commerce-subscriptions-simple-public-object-input
- name: Subscription
  property_count: 6
  slug: hubspot-commerce-subscriptions-subscription
- name: ActorCollection
  property_count: 2
  slug: hubspot-conversations-actor-collection
- name: Actor
  property_count: 5
  slug: hubspot-conversations-actor
- name: Attachment
  property_count: 5
  slug: hubspot-conversations-attachment
- name: ChannelCollection
  property_count: 2
  slug: hubspot-conversations-channel-collection
- name: Channel
  property_count: 5
  slug: hubspot-conversations-channel
- name: ErrorDetail
  property_count: 5
  slug: hubspot-conversations-error-detail
- name: Error
  property_count: 7
  slug: hubspot-conversations-error
- name: InboxCollection
  property_count: 3
  slug: hubspot-conversations-inbox-collection
- name: Inbox
  property_count: 6
  slug: hubspot-conversations-inbox
- name: MessageCollection
  property_count: 2
  slug: hubspot-conversations-message-collection
- name: MessageRecipient
  property_count: 1
  slug: hubspot-conversations-message-recipient
- name: Message
  property_count: 13
  slug: hubspot-conversations-message
- name: MessageStatus
  property_count: 1
  slug: hubspot-conversations-message-status
- name: PagingNext
  property_count: 2
  slug: hubspot-conversations-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-conversations-paging
- name: SendMessageRequest
  property_count: 7
  slug: hubspot-conversations-send-message-request
- name: ThreadCollection
  property_count: 2
  slug: hubspot-conversations-thread-collection
- name: Thread
  property_count: 14
  slug: hubspot-conversations-thread
- name: UpdateThreadRequest
  property_count: 2
  slug: hubspot-conversations-update-thread-request
- name: AssociationDefinitionCollection
  property_count: 2
  slug: hubspot-crm-associations-association-definition-collection
- name: AssociationDefinition
  property_count: 7
  slug: hubspot-crm-associations-association-definition
- name: AssociationLabelCollection
  property_count: 2
  slug: hubspot-crm-associations-association-label-collection
- name: AssociationLabel
  property_count: 3
  slug: hubspot-crm-associations-association-label
- name: AssociationResult
  property_count: 3
  slug: hubspot-crm-associations-association-result
- name: Association
  property_count: 2
  slug: hubspot-crm-associations-association
- name: AssociationTypeInput
  property_count: 2
  slug: hubspot-crm-associations-association-type-input
- name: AssociationType
  property_count: 3
  slug: hubspot-crm-associations-association-type
- name: BatchAssociationArchiveInput
  property_count: 1
  slug: hubspot-crm-associations-batch-association-archive-input
- name: BatchAssociationArchiveItem
  property_count: 3
  slug: hubspot-crm-associations-batch-association-archive-item
- name: BatchAssociationCreateInput
  property_count: 1
  slug: hubspot-crm-associations-batch-association-create-input
- name: BatchAssociationCreateItem
  property_count: 3
  slug: hubspot-crm-associations-batch-association-create-item
- name: BatchAssociationReadInput
  property_count: 1
  slug: hubspot-crm-associations-batch-association-read-input
- name: BatchAssociationResponse
  property_count: 8
  slug: hubspot-crm-associations-batch-association-response
- name: CreateAssociationInput
  property_count: 2
  slug: hubspot-crm-associations-create-association-input
- name: CreateLabelInput
  property_count: 3
  slug: hubspot-crm-associations-create-label-input
- name: ErrorDetail
  property_count: 5
  slug: hubspot-crm-associations-error-detail
- name: Error
  property_count: 7
  slug: hubspot-crm-associations-error
- name: ObjectReference
  property_count: 1
  slug: hubspot-crm-associations-object-reference
- name: PagingNext
  property_count: 2
  slug: hubspot-crm-associations-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-crm-associations-paging
- name: StandardError
  property_count: 7
  slug: hubspot-crm-associations-standard-error
- name: Association
  property_count: 2
  slug: hubspot-crm-companies-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-companies-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-companies-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-companies-batch-read-input
- name: BatchResponseCompany
  property_count: 3
  slug: hubspot-crm-companies-batch-response-company
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-companies-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-companies-collection-response-association
- name: CollectionResponseCompany
  property_count: 2
  slug: hubspot-crm-companies-collection-response-company
- name: Company
  property_count: 6
  slug: hubspot-crm-companies-company
- name: Error
  property_count: 4
  slug: hubspot-crm-companies-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-companies-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-companies-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-companies-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-companies-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-companies-simple-public-object-input
- name: Association
  property_count: 2
  slug: hubspot-crm-contacts-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-contacts-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-contacts-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-contacts-batch-read-input
- name: BatchResponseContact
  property_count: 3
  slug: hubspot-crm-contacts-batch-response-contact
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-contacts-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-association
- name: CollectionResponseContact
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-contact
- name: Contact
  property_count: 6
  slug: hubspot-crm-contacts-contact
- name: Error
  property_count: 4
  slug: hubspot-crm-contacts-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-contacts-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-contacts-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-contacts-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-contacts-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-contacts-simple-public-object-input
- name: Association
  property_count: 2
  slug: hubspot-crm-deals-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-deals-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-deals-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-deals-batch-read-input
- name: BatchResponseDeal
  property_count: 3
  slug: hubspot-crm-deals-batch-response-deal
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-deals-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-deals-collection-response-association
- name: CollectionResponseDeal
  property_count: 2
  slug: hubspot-crm-deals-collection-response-deal
- name: Deal
  property_count: 6
  slug: hubspot-crm-deals-deal
- name: Error
  property_count: 4
  slug: hubspot-crm-deals-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-deals-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-deals-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-deals-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-deals-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-deals-simple-public-object-input
- name: BatchDeleteInputItem
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input-item
- name: BatchDeleteInput
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input
- name: BatchError
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-error
- name: BatchPortalFlagStateInputItem
  property_count: 2
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-item
- name: BatchPortalFlagStateInput
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input
- name: BatchPortalFlagStateResponse
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response
- name: BatchPortalFlagStateResponseWithErrors
  property_count: 5
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-with-errors
- name: ErrorDetail
  property_count: 5
  slug: hubspot-crm-feature-flags-error-detail
- name: Error
  property_count: 7
  slug: hubspot-crm-feature-flags-error
- name: FeatureFlagInput
  property_count: 1
  slug: hubspot-crm-feature-flags-feature-flag-input
- name: FeatureFlag
  property_count: 4
  slug: hubspot-crm-feature-flags-feature-flag
- name: FlagState
  property_count: 0
  slug: hubspot-crm-feature-flags-flag-state
- name: PagingNext
  property_count: 2
  slug: hubspot-crm-feature-flags-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-crm-feature-flags-paging
- name: PortalFlagStateCollection
  property_count: 2
  slug: hubspot-crm-feature-flags-portal-flag-state-collection
- name: PortalFlagStateInput
  property_count: 1
  slug: hubspot-crm-feature-flags-portal-flag-state-input
- name: PortalFlagState
  property_count: 4
  slug: hubspot-crm-feature-flags-portal-flag-state
- name: CollectionResponseList
  property_count: 2
  slug: hubspot-crm-lists-collection-response-list
- name: CollectionResponseMembership
  property_count: 2
  slug: hubspot-crm-lists-collection-response-membership
- name: Error
  property_count: 4
  slug: hubspot-crm-lists-error
- name: ListCreateRequest
  property_count: 4
  slug: hubspot-crm-lists-list-create-request
- name: List
  property_count: 9
  slug: hubspot-crm-lists-list
- name: MembershipChangeRequest
  property_count: 2
  slug: hubspot-crm-lists-membership-change-request
- name: MembershipChangeResponse
  property_count: 4
  slug: hubspot-crm-lists-membership-change-response
- name: Membership
  property_count: 2
  slug: hubspot-crm-lists-membership
- name: Paging
  property_count: 1
  slug: hubspot-crm-lists-paging
- name: HubSpot CRM Object
  property_count: 8
  slug: hubspot-crm-object
- name: CRMObject
  property_count: 5
  slug: hubspot-crm-search-crm-object
- name: Error
  property_count: 5
  slug: hubspot-crm-search-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-search-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-crm-search-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-search-paging
- name: HubSpot CRM Search Request
  property_count: 6
  slug: hubspot-crm-search-request
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-search-search-request
- name: SearchResponse
  property_count: 3
  slug: hubspot-crm-search-search-response
- name: Sort
  property_count: 2
  slug: hubspot-crm-search-sort
- name: Association
  property_count: 2
  slug: hubspot-crm-tickets-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-tickets-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-tickets-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-tickets-batch-read-input
- name: BatchResponseTicket
  property_count: 3
  slug: hubspot-crm-tickets-batch-response-ticket
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-tickets-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-association
- name: CollectionResponseTicket
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-ticket
- name: Error
  property_count: 4
  slug: hubspot-crm-tickets-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-tickets-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-tickets-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-tickets-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-tickets-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-tickets-simple-public-object-input
- name: Ticket
  property_count: 6
  slug: hubspot-crm-tickets-ticket
- name: ActionDefinitionCollection
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-collection
- name: ActionDefinitionInput
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-input
- name: ActionDefinitionPatch
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-patch
- name: ActionDefinitionRevisionCollection
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-revision-collection
- name: ActionDefinitionRevision
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-definition-revision
- name: ActionDefinition
  property_count: 10
  slug: hubspot-custom-workflow-actions-action-definition
- name: ActionFunctionCollection
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-collection
- name: ActionFunctionInput
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-input
- name: ActionFunctionReference
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-function-reference
- name: ActionFunction
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-function
- name: ActionLabels
  property_count: 4
  slug: hubspot-custom-workflow-actions-action-labels
- name: BatchCallbackCompletionRequest
  property_count: 1
  slug: hubspot-custom-workflow-actions-batch-callback-completion-request
- name: BatchCallbackError
  property_count: 3
  slug: hubspot-custom-workflow-actions-batch-callback-error
- name: BatchCallbackInput
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-input
- name: BatchCallbackResponse
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-response
- name: CallbackCompletionRequest
  property_count: 1
  slug: hubspot-custom-workflow-actions-callback-completion-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-custom-workflow-actions-error-detail
- name: Error
  property_count: 7
  slug: hubspot-custom-workflow-actions-error
- name: FieldOption
  property_count: 3
  slug: hubspot-custom-workflow-actions-field-option
- name: FieldTypeDefinition
  property_count: 6
  slug: hubspot-custom-workflow-actions-field-type-definition
- name: InputField
  property_count: 3
  slug: hubspot-custom-workflow-actions-input-field
- name: ObjectRequestOptions
  property_count: 1
  slug: hubspot-custom-workflow-actions-object-request-options
- name: OutputField
  property_count: 1
  slug: hubspot-custom-workflow-actions-output-field
- name: Paging
  property_count: 1
  slug: hubspot-custom-workflow-actions-paging
- name: DomainCollectionResponse
  property_count: 3
  slug: hubspot-domains-domain-collection-response
- name: Domain
  property_count: 21
  slug: hubspot-domains-domain
- name: ErrorDetail
  property_count: 5
  slug: hubspot-domains-error-detail
- name: Error
  property_count: 7
  slug: hubspot-domains-error
- name: ForwardPaging
  property_count: 1
  slug: hubspot-domains-forward-paging
- name: NextPage
  property_count: 2
  slug: hubspot-domains-next-page
- name: AssociationInput
  property_count: 2
  slug: hubspot-engagement-calls-association-input
- name: AssociationType
  property_count: 2
  slug: hubspot-engagement-calls-association-type
- name: BatchArchiveCallsRequest
  property_count: 1
  slug: hubspot-engagement-calls-batch-archive-calls-request
- name: BatchCallsResponse
  property_count: 7
  slug: hubspot-engagement-calls-batch-calls-response
- name: BatchCreateCallsRequest
  property_count: 1
  slug: hubspot-engagement-calls-batch-create-calls-request
- name: BatchError
  property_count: 5
  slug: hubspot-engagement-calls-batch-error
- name: BatchReadCallsRequest
  property_count: 4
  slug: hubspot-engagement-calls-batch-read-calls-request
- name: BatchReadInput
  property_count: 1
  slug: hubspot-engagement-calls-batch-read-input
- name: BatchUpdateCallsRequest
  property_count: 1
  slug: hubspot-engagement-calls-batch-update-calls-request
- name: BatchUpdateInput
  property_count: 2
  slug: hubspot-engagement-calls-batch-update-input
- name: CallCollectionResponse
  property_count: 2
  slug: hubspot-engagement-calls-call-collection-response
- name: CallCreateRequest
  property_count: 2
  slug: hubspot-engagement-calls-call-create-request
- name: Call
  property_count: 7
  slug: hubspot-engagement-calls-call
- name: CallSearchRequest
  property_count: 6
  slug: hubspot-engagement-calls-call-search-request
- name: CallSearchResponse
  property_count: 3
  slug: hubspot-engagement-calls-call-search-response
- name: CallUpdateRequest
  property_count: 1
  slug: hubspot-engagement-calls-call-update-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-engagement-calls-error-detail
- name: Error
  property_count: 7
  slug: hubspot-engagement-calls-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-calls-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-engagement-calls-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: hubspot-engagement-calls-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: hubspot-engagement-calls-next-page
- name: Paging
  property_count: 1
  slug: hubspot-engagement-calls-paging
- name: PropertyHistory
  property_count: 6
  slug: hubspot-engagement-calls-property-history
- name: SortOption
  property_count: 2
  slug: hubspot-engagement-calls-sort-option
- name: Association
  property_count: 2
  slug: hubspot-engagement-emails-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-engagement-emails-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-engagement-emails-batch-read-input
- name: BatchResponseEmailEngagement
  property_count: 3
  slug: hubspot-engagement-emails-batch-response-email-engagement
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-engagement-emails-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-association
- name: CollectionResponseEmailEngagement
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-email-engagement
- name: EmailEngagement
  property_count: 6
  slug: hubspot-engagement-emails-email-engagement
- name: Error
  property_count: 4
  slug: hubspot-engagement-emails-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-emails-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-engagement-emails-filter
- name: Paging
  property_count: 1
  slug: hubspot-engagement-emails-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-engagement-emails-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-engagement-emails-simple-public-object-input
- name: Association
  property_count: 2
  slug: hubspot-engagement-meetings-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-engagement-meetings-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-engagement-meetings-batch-read-input
- name: BatchResponseMeeting
  property_count: 3
  slug: hubspot-engagement-meetings-batch-response-meeting
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-engagement-meetings-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-association
- name: CollectionResponseMeeting
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-meeting
- name: Error
  property_count: 4
  slug: hubspot-engagement-meetings-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-meetings-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-engagement-meetings-filter
- name: Meeting
  property_count: 6
  slug: hubspot-engagement-meetings-meeting
- name: Paging
  property_count: 1
  slug: hubspot-engagement-meetings-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-engagement-meetings-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-engagement-meetings-simple-public-object-input
- name: AssociationInput
  property_count: 2
  slug: hubspot-engagement-notes-association-input
- name: AssociationType
  property_count: 2
  slug: hubspot-engagement-notes-association-type
- name: BatchArchiveNotesRequest
  property_count: 1
  slug: hubspot-engagement-notes-batch-archive-notes-request
- name: BatchCreateNotesRequest
  property_count: 1
  slug: hubspot-engagement-notes-batch-create-notes-request
- name: BatchError
  property_count: 5
  slug: hubspot-engagement-notes-batch-error
- name: BatchNotesResponse
  property_count: 7
  slug: hubspot-engagement-notes-batch-notes-response
- name: BatchReadInput
  property_count: 1
  slug: hubspot-engagement-notes-batch-read-input
- name: BatchReadNotesRequest
  property_count: 4
  slug: hubspot-engagement-notes-batch-read-notes-request
- name: BatchUpdateInput
  property_count: 2
  slug: hubspot-engagement-notes-batch-update-input
- name: BatchUpdateNotesRequest
  property_count: 1
  slug: hubspot-engagement-notes-batch-update-notes-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-engagement-notes-error-detail
- name: Error
  property_count: 7
  slug: hubspot-engagement-notes-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-notes-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-engagement-notes-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: hubspot-engagement-notes-next-page
- name: NoteCollectionResponse
  property_count: 2
  slug: hubspot-engagement-notes-note-collection-response
- name: NoteCreateRequest
  property_count: 2
  slug: hubspot-engagement-notes-note-create-request
- name: Note
  property_count: 7
  slug: hubspot-engagement-notes-note
- name: NoteSearchRequest
  property_count: 6
  slug: hubspot-engagement-notes-note-search-request
- name: NoteSearchResponse
  property_count: 3
  slug: hubspot-engagement-notes-note-search-response
- name: NoteUpdateRequest
  property_count: 1
  slug: hubspot-engagement-notes-note-update-request
- name: Paging
  property_count: 1
  slug: hubspot-engagement-notes-paging
- name: PropertyHistory
  property_count: 6
  slug: hubspot-engagement-notes-property-history
- name: SortOption
  property_count: 2
  slug: hubspot-engagement-notes-sort-option
- name: Association
  property_count: 2
  slug: hubspot-engagement-tasks-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-engagement-tasks-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-engagement-tasks-batch-read-input
- name: BatchResponseTask
  property_count: 3
  slug: hubspot-engagement-tasks-batch-response-task
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-engagement-tasks-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-association
- name: CollectionResponseTask
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-task
- name: Error
  property_count: 4
  slug: hubspot-engagement-tasks-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-tasks-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-engagement-tasks-filter
- name: Paging
  property_count: 1
  slug: hubspot-engagement-tasks-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-engagement-tasks-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-engagement-tasks-simple-public-object-input
- name: Task
  property_count: 6
  slug: hubspot-engagement-tasks-task
- name: EmailMessage
  property_count: 6
  slug: hubspot-marketing-emal-email-message
- name: ErrorDetail
  property_count: 5
  slug: hubspot-marketing-emal-error-detail
- name: Error
  property_count: 7
  slug: hubspot-marketing-emal-error
- name: NextPage
  property_count: 2
  slug: hubspot-marketing-emal-next-page
- name: Paging
  property_count: 1
  slug: hubspot-marketing-emal-paging
- name: SmtpTokenCollectionResponse
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-collection-response
- name: SmtpTokenCreateRequest
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-create-request
- name: SmtpToken
  property_count: 6
  slug: hubspot-marketing-emal-smtp-token
- name: SmtpTokenWithPassword
  property_count: 7
  slug: hubspot-marketing-emal-smtp-token-with-password
- name: TransactionalEmailRequest
  property_count: 4
  slug: hubspot-marketing-emal-transactional-email-request
- name: TransactionalEmailResponse
  property_count: 6
  slug: hubspot-marketing-emal-transactional-email-response
- name: AccessTokenMetadata
  property_count: 9
  slug: hubspot-oauth-access-token-metadata
- name: ErrorDetail
  property_count: 5
  slug: hubspot-oauth-error-detail
- name: Error
  property_count: 7
  slug: hubspot-oauth-error
- name: RefreshTokenMetadata
  property_count: 6
  slug: hubspot-oauth-refresh-token-metadata
- name: TokenRequest
  property_count: 6
  slug: hubspot-oauth-token-request
- name: TokenResponse
  property_count: 5
  slug: hubspot-oauth-token-response
- name: ActionResponse
  property_count: 5
  slug: hubspot-source-code-action-response
- name: AssetFileMetadata
  property_count: 8
  slug: hubspot-source-code-asset-file-metadata
- name: ErrorDetail
  property_count: 5
  slug: hubspot-source-code-error-detail
- name: Error
  property_count: 7
  slug: hubspot-source-code-error
- name: FileExtractRequest
  property_count: 1
  slug: hubspot-source-code-file-extract-request
- name: FileUploadRequest
  property_count: 1
  slug: hubspot-source-code-file-upload-request
- name: TaskLocator
  property_count: 2
  slug: hubspot-source-code-task-locator
- name: ValidationError
  property_count: 4
  slug: hubspot-source-code-validation-error
- name: ValidationResult
  property_count: 3
  slug: hubspot-source-code-validation-result
- name: ValidationWarning
  property_count: 3
  slug: hubspot-source-code-validation-warning
- name: EmailMessage
  property_count: 6
  slug: marketing-emal-api-email-message
- name: NextPage
  property_count: 2
  slug: marketing-emal-api-next-page
- name: Paging
  property_count: 1
  slug: marketing-emal-api-paging
- name: SmtpTokenCollectionResponse
  property_count: 2
  slug: marketing-emal-api-smtp-token-collection-response
- name: SmtpTokenCreateRequest
  property_count: 2
  slug: marketing-emal-api-smtp-token-create-request
- name: SmtpToken
  property_count: 6
  slug: marketing-emal-api-smtp-token
- name: SmtpTokenWithPassword
  property_count: 7
  slug: marketing-emal-api-smtp-token-with-password
- name: TransactionalEmailRequest
  property_count: 4
  slug: marketing-emal-api-transactional-email-request
- name: TransactionalEmailResponse
  property_count: 6
  slug: marketing-emal-api-transactional-email-response
- name: AccessTokenMetadata
  property_count: 9
  slug: oauth-api-access-token-metadata
- name: RefreshTokenMetadata
  property_count: 6
  slug: oauth-api-refresh-token-metadata
- name: TokenRequest
  property_count: 6
  slug: oauth-api-token-request
- name: TokenResponse
  property_count: 5
  slug: oauth-api-token-response
- name: ActionResponse
  property_count: 5
  slug: source-code-api-action-response
- name: AssetFileMetadata
  property_count: 8
  slug: source-code-api-asset-file-metadata
- name: FileExtractRequest
  property_count: 1
  slug: source-code-api-file-extract-request
- name: FileUploadRequest
  property_count: 1
  slug: source-code-api-file-upload-request
- name: TaskLocator
  property_count: 2
  slug: source-code-api-task-locator
- name: ValidationError
  property_count: 4
  slug: source-code-api-validation-error
- name: ValidationResult
  property_count: 3
  slug: source-code-api-validation-result
- name: ValidationWarning
  property_count: 3
  slug: source-code-api-validation-warning
json_structures:
- name: Analytics Events Api Event Instance Collection Structure
  property_count: 2
  slug: analytics-events-api-event-instance-collection-structure
- name: Analytics Events Api Event Instance Structure
  property_count: 6
  slug: analytics-events-api-event-instance-structure
- name: Analytics Events Api Event Type Collection Structure
  property_count: 1
  slug: analytics-events-api-event-type-collection-structure
- name: Analytics Events Api Paging Next Structure
  property_count: 2
  slug: analytics-events-api-paging-next-structure
- name: Analytics Events Api Paging Previous Structure
  property_count: 2
  slug: analytics-events-api-paging-previous-structure
- name: Analytics Events Api Paging Structure
  property_count: 2
  slug: analytics-events-api-paging-structure
- name: Authors Api Attach To Language Group Request Structure
  property_count: 4
  slug: authors-api-attach-to-language-group-request-structure
- name: Authors Api Batch Archive Input Structure
  property_count: 1
  slug: authors-api-batch-archive-input-structure
- name: Authors Api Batch Create Input Structure
  property_count: 1
  slug: authors-api-batch-create-input-structure
- name: Authors Api Batch Input Item Structure
  property_count: 2
  slug: authors-api-batch-input-item-structure
- name: Authors Api Batch Input Structure
  property_count: 1
  slug: authors-api-batch-input-structure
- name: Authors Api Batch Read Input Structure
  property_count: 1
  slug: authors-api-batch-read-input-structure
- name: Authors Api Batch Response Structure
  property_count: 6
  slug: authors-api-batch-response-structure
- name: Authors Api Batch Response With Errors Structure
  property_count: 0
  slug: authors-api-batch-response-with-errors-structure
- name: Authors Api Blog Author Collection Structure
  property_count: 3
  slug: authors-api-blog-author-collection-structure
- name: Authors Api Blog Author Input Structure
  property_count: 9
  slug: authors-api-blog-author-input-structure
- name: Authors Api Blog Author Structure
  property_count: 15
  slug: authors-api-blog-author-structure
- name: Authors Api Create Language Variation Request Structure
  property_count: 2
  slug: authors-api-create-language-variation-request-structure
- name: Authors Api Detach From Language Group Request Structure
  property_count: 1
  slug: authors-api-detach-from-language-group-request-structure
- name: Authors Api Paging Next Structure
  property_count: 2
  slug: authors-api-paging-next-structure
- name: Authors Api Paging Structure
  property_count: 1
  slug: authors-api-paging-structure
- name: Authors Api Set Language Primary Request Structure
  property_count: 1
  slug: authors-api-set-language-primary-request-structure
- name: Blog Posts Api Attach To Language Group Request Structure
  property_count: 4
  slug: blog-posts-api-attach-to-language-group-request-structure
- name: Blog Posts Api Batch Input Item Structure
  property_count: 1
  slug: blog-posts-api-batch-input-item-structure
- name: Blog Posts Api Batch Input Structure
  property_count: 1
  slug: blog-posts-api-batch-input-structure
- name: Blog Posts Api Batch Response Structure
  property_count: 6
  slug: blog-posts-api-batch-response-structure
- name: Blog Posts Api Batch Response With Errors Structure
  property_count: 0
  slug: blog-posts-api-batch-response-with-errors-structure
- name: Blog Posts Api Blog Post Collection Structure
  property_count: 3
  slug: blog-posts-api-blog-post-collection-structure
- name: Blog Posts Api Blog Post Input Structure
  property_count: 15
  slug: blog-posts-api-blog-post-input-structure
- name: Blog Posts Api Blog Post Structure
  property_count: 32
  slug: blog-posts-api-blog-post-structure
- name: Blog Posts Api Clone Request Structure
  property_count: 1
  slug: blog-posts-api-clone-request-structure
- name: Blog Posts Api Create Language Variation Request Structure
  property_count: 2
  slug: blog-posts-api-create-language-variation-request-structure
- name: Blog Posts Api Detach From Language Group Request Structure
  property_count: 1
  slug: blog-posts-api-detach-from-language-group-request-structure
- name: Blog Posts Api Paging Next Structure
  property_count: 2
  slug: blog-posts-api-paging-next-structure
- name: Blog Posts Api Paging Previous Structure
  property_count: 2
  slug: blog-posts-api-paging-previous-structure
- name: Blog Posts Api Paging Structure
  property_count: 2
  slug: blog-posts-api-paging-structure
- name: Blog Posts Api Push Live Request Structure
  property_count: 1
  slug: blog-posts-api-push-live-request-structure
- name: Blog Posts Api Reset Draft Request Structure
  property_count: 1
  slug: blog-posts-api-reset-draft-request-structure
- name: Blog Posts Api Restore Previous Version Request Structure
  property_count: 2
  slug: blog-posts-api-restore-previous-version-request-structure
- name: Blog Posts Api Schedule Request Structure
  property_count: 2
  slug: blog-posts-api-schedule-request-structure
- name: Blog Posts Api Set Language Primary Request Structure
  property_count: 1
  slug: blog-posts-api-set-language-primary-request-structure
- name: Blog Posts Api Version History Structure
  property_count: 4
  slug: blog-posts-api-version-history-structure
- name: Cms Hubdb Api Collection Response Hub Dbrow Structure
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbrow-structure
- name: Cms Hubdb Api Collection Response Hub Dbtable Structure
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbtable-structure
- name: Cms Hubdb Api Hub Dbcolumn Structure
  property_count: 5
  slug: cms-hubdb-api-hub-dbcolumn-structure
- name: Cms Hubdb Api Hub Dbrow Create Request Structure
  property_count: 1
  slug: cms-hubdb-api-hub-dbrow-create-request-structure
- name: Cms Hubdb Api Hub Dbrow Structure
  property_count: 4
  slug: cms-hubdb-api-hub-dbrow-structure
- name: Cms Hubdb Api Hub Dbtable Create Request Structure
  property_count: 3
  slug: cms-hubdb-api-hub-dbtable-create-request-structure
- name: Cms Hubdb Api Hub Dbtable Structure
  property_count: 9
  slug: cms-hubdb-api-hub-dbtable-structure
- name: Cms Hubdb Api Paging Structure
  property_count: 1
  slug: cms-hubdb-api-paging-structure
- name: Cms Pages Api Collection Response Page Structure
  property_count: 2
  slug: cms-pages-api-collection-response-page-structure
- name: Cms Pages Api Page Create Request Structure
  property_count: 8
  slug: cms-pages-api-page-create-request-structure
- name: Cms Pages Api Page Structure
  property_count: 16
  slug: cms-pages-api-page-structure
- name: Cms Pages Api Page Update Request Structure
  property_count: 5
  slug: cms-pages-api-page-update-request-structure
- name: Cms Pages Api Paging Structure
  property_count: 1
  slug: cms-pages-api-paging-structure
- name: Commerce Payments Api Association Input Structure
  property_count: 2
  slug: commerce-payments-api-association-input-structure
- name: Commerce Payments Api Association Result Structure
  property_count: 2
  slug: commerce-payments-api-association-result-structure
- name: Commerce Payments Api Association Type Structure
  property_count: 2
  slug: commerce-payments-api-association-type-structure
- name: Commerce Payments Api Batch Archive Request Structure
  property_count: 1
  slug: commerce-payments-api-batch-archive-request-structure
- name: Commerce Payments Api Batch Create Request Structure
  property_count: 1
  slug: commerce-payments-api-batch-create-request-structure
- name: Commerce Payments Api Batch Create Response Structure
  property_count: 8
  slug: commerce-payments-api-batch-create-response-structure
- name: Commerce Payments Api Batch Error Structure
  property_count: 8
  slug: commerce-payments-api-batch-error-structure
- name: Commerce Payments Api Batch Read Input Item Structure
  property_count: 1
  slug: commerce-payments-api-batch-read-input-item-structure
- name: Commerce Payments Api Batch Read Request Structure
  property_count: 4
  slug: commerce-payments-api-batch-read-request-structure
- name: Commerce Payments Api Batch Read Response Structure
  property_count: 8
  slug: commerce-payments-api-batch-read-response-structure
- name: Commerce Payments Api Batch Update Input Item Structure
  property_count: 3
  slug: commerce-payments-api-batch-update-input-item-structure
- name: Commerce Payments Api Batch Update Request Structure
  property_count: 1
  slug: commerce-payments-api-batch-update-request-structure
- name: Commerce Payments Api Batch Update Response Structure
  property_count: 8
  slug: commerce-payments-api-batch-update-response-structure
- name: Commerce Payments Api Commerce Payment Collection Structure
  property_count: 2
  slug: commerce-payments-api-commerce-payment-collection-structure
- name: Commerce Payments Api Commerce Payment Input Structure
  property_count: 2
  slug: commerce-payments-api-commerce-payment-input-structure
- name: Commerce Payments Api Commerce Payment Patch Structure
  property_count: 1
  slug: commerce-payments-api-commerce-payment-patch-structure
- name: Commerce Payments Api Commerce Payment Structure
  property_count: 8
  slug: commerce-payments-api-commerce-payment-structure
- name: Commerce Payments Api Filter Group Structure
  property_count: 1
  slug: commerce-payments-api-filter-group-structure
- name: Commerce Payments Api Filter Structure
  property_count: 5
  slug: commerce-payments-api-filter-structure
- name: Commerce Payments Api Paging Structure
  property_count: 2
  slug: commerce-payments-api-paging-structure
- name: Commerce Payments Api Property History Structure
  property_count: 6
  slug: commerce-payments-api-property-history-structure
- name: Commerce Payments Api Search Request Structure
  property_count: 6
  slug: commerce-payments-api-search-request-structure
- name: Commerce Payments Api Search Response Structure
  property_count: 3
  slug: commerce-payments-api-search-response-structure
- name: Commerce Payments Api Sort Option Structure
  property_count: 2
  slug: commerce-payments-api-sort-option-structure
- name: Commerce Subscriptions Api Association Structure
  property_count: 2
  slug: commerce-subscriptions-api-association-structure
- name: Commerce Subscriptions Api Batch Create Input Structure
  property_count: 1
  slug: commerce-subscriptions-api-batch-create-input-structure
- name: Commerce Subscriptions Api Batch Read Input Structure
  property_count: 2
  slug: commerce-subscriptions-api-batch-read-input-structure
- name: Commerce Subscriptions Api Batch Response Subscription Structure
  property_count: 3
  slug: commerce-subscriptions-api-batch-response-subscription-structure
- name: Commerce Subscriptions Api Batch Update Input Structure
  property_count: 1
  slug: commerce-subscriptions-api-batch-update-input-structure
- name: Commerce Subscriptions Api Collection Response Association Structure
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-association-structure
- name: Commerce Subscriptions Api Collection Response Subscription Structure
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-subscription-structure
- name: Commerce Subscriptions Api Filter Group Structure
  property_count: 1
  slug: commerce-subscriptions-api-filter-group-structure
- name: Commerce Subscriptions Api Filter Structure
  property_count: 3
  slug: commerce-subscriptions-api-filter-structure
- name: Commerce Subscriptions Api Paging Structure
  property_count: 1
  slug: commerce-subscriptions-api-paging-structure
- name: Commerce Subscriptions Api Search Request Structure
  property_count: 6
  slug: commerce-subscriptions-api-search-request-structure
- name: Commerce Subscriptions Api Simple Public Object Input Structure
  property_count: 1
  slug: commerce-subscriptions-api-simple-public-object-input-structure
- name: Commerce Subscriptions Api Subscription Structure
  property_count: 6
  slug: commerce-subscriptions-api-subscription-structure
- name: Conversations Api Actor Collection Structure
  property_count: 2
  slug: conversations-api-actor-collection-structure
- name: Conversations Api Actor Structure
  property_count: 5
  slug: conversations-api-actor-structure
- name: Conversations Api Attachment Structure
  property_count: 5
  slug: conversations-api-attachment-structure
- name: Conversations Api Channel Collection Structure
  property_count: 2
  slug: conversations-api-channel-collection-structure
- name: Conversations Api Channel Structure
  property_count: 5
  slug: conversations-api-channel-structure
- name: Conversations Api Inbox Collection Structure
  property_count: 3
  slug: conversations-api-inbox-collection-structure
- name: Conversations Api Inbox Structure
  property_count: 6
  slug: conversations-api-inbox-structure
- name: Conversations Api Message Collection Structure
  property_count: 2
  slug: conversations-api-message-collection-structure
- name: Conversations Api Message Recipient Structure
  property_count: 1
  slug: conversations-api-message-recipient-structure
- name: Conversations Api Message Status Structure
  property_count: 1
  slug: conversations-api-message-status-structure
- name: Conversations Api Message Structure
  property_count: 13
  slug: conversations-api-message-structure
- name: Conversations Api Paging Next Structure
  property_count: 2
  slug: conversations-api-paging-next-structure
- name: Conversations Api Paging Structure
  property_count: 1
  slug: conversations-api-paging-structure
- name: Conversations Api Send Message Request Structure
  property_count: 7
  slug: conversations-api-send-message-request-structure
- name: Conversations Api Thread Collection Structure
  property_count: 2
  slug: conversations-api-thread-collection-structure
- name: Conversations Api Thread Structure
  property_count: 14
  slug: conversations-api-thread-structure
- name: Conversations Api Update Thread Request Structure
  property_count: 2
  slug: conversations-api-update-thread-request-structure
- name: Crm Associations Api Association Definition Collection Structure
  property_count: 2
  slug: crm-associations-api-association-definition-collection-structure
- name: Crm Associations Api Association Definition Structure
  property_count: 7
  slug: crm-associations-api-association-definition-structure
- name: Crm Associations Api Association Label Collection Structure
  property_count: 2
  slug: crm-associations-api-association-label-collection-structure
- name: Crm Associations Api Association Label Structure
  property_count: 3
  slug: crm-associations-api-association-label-structure
- name: Crm Associations Api Association Result Structure
  property_count: 3
  slug: crm-associations-api-association-result-structure
- name: Crm Associations Api Association Structure
  property_count: 2
  slug: crm-associations-api-association-structure
- name: Crm Associations Api Association Type Input Structure
  property_count: 2
  slug: crm-associations-api-association-type-input-structure
- name: Crm Associations Api Association Type Structure
  property_count: 3
  slug: crm-associations-api-association-type-structure
- name: Crm Associations Api Batch Association Archive Input Structure
  property_count: 1
  slug: crm-associations-api-batch-association-archive-input-structure
- name: Crm Associations Api Batch Association Archive Item Structure
  property_count: 3
  slug: crm-associations-api-batch-association-archive-item-structure
- name: Crm Associations Api Batch Association Create Input Structure
  property_count: 1
  slug: crm-associations-api-batch-association-create-input-structure
- name: Crm Associations Api Batch Association Create Item Structure
  property_count: 3
  slug: crm-associations-api-batch-association-create-item-structure
- name: Crm Associations Api Batch Association Read Input Structure
  property_count: 1
  slug: crm-associations-api-batch-association-read-input-structure
- name: Crm Associations Api Batch Association Response Structure
  property_count: 8
  slug: crm-associations-api-batch-association-response-structure
- name: Crm Associations Api Create Association Input Structure
  property_count: 2
  slug: crm-associations-api-create-association-input-structure
- name: Crm Associations Api Create Label Input Structure
  property_count: 3
  slug: crm-associations-api-create-label-input-structure
- name: Crm Associations Api Object Reference Structure
  property_count: 1
  slug: crm-associations-api-object-reference-structure
- name: Crm Associations Api Paging Next Structure
  property_count: 2
  slug: crm-associations-api-paging-next-structure
- name: Crm Associations Api Paging Structure
  property_count: 1
  slug: crm-associations-api-paging-structure
- name: Crm Companies Api Association Structure
  property_count: 2
  slug: crm-companies-api-association-structure
- name: Crm Companies Api Batch Archive Input Structure
  property_count: 1
  slug: crm-companies-api-batch-archive-input-structure
- name: Crm Companies Api Batch Create Input Structure
  property_count: 1
  slug: crm-companies-api-batch-create-input-structure
- name: Crm Companies Api Batch Read Input Structure
  property_count: 2
  slug: crm-companies-api-batch-read-input-structure
- name: Crm Companies Api Batch Response Company Structure
  property_count: 3
  slug: crm-companies-api-batch-response-company-structure
- name: Crm Companies Api Batch Update Input Structure
  property_count: 1
  slug: crm-companies-api-batch-update-input-structure
- name: Crm Companies Api Collection Response Association Structure
  property_count: 2
  slug: crm-companies-api-collection-response-association-structure
- name: Crm Companies Api Collection Response Company Structure
  property_count: 2
  slug: crm-companies-api-collection-response-company-structure
- name: Crm Companies Api Company Structure
  property_count: 6
  slug: crm-companies-api-company-structure
- name: Crm Companies Api Filter Group Structure
  property_count: 1
  slug: crm-companies-api-filter-group-structure
- name: Crm Companies Api Filter Structure
  property_count: 3
  slug: crm-companies-api-filter-structure
- name: Crm Companies Api Paging Structure
  property_count: 1
  slug: crm-companies-api-paging-structure
- name: Crm Companies Api Search Request Structure
  property_count: 6
  slug: crm-companies-api-search-request-structure
- name: Crm Companies Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-companies-api-simple-public-object-input-structure
- name: Crm Contacts Api Association Structure
  property_count: 2
  slug: crm-contacts-api-association-structure
- name: Crm Contacts Api Batch Archive Input Structure
  property_count: 1
  slug: crm-contacts-api-batch-archive-input-structure
- name: Crm Contacts Api Batch Create Input Structure
  property_count: 1
  slug: crm-contacts-api-batch-create-input-structure
- name: Crm Contacts Api Batch Read Input Structure
  property_count: 2
  slug: crm-contacts-api-batch-read-input-structure
- name: Crm Contacts Api Batch Response Contact Structure
  property_count: 3
  slug: crm-contacts-api-batch-response-contact-structure
- name: Crm Contacts Api Batch Update Input Structure
  property_count: 1
  slug: crm-contacts-api-batch-update-input-structure
- name: Crm Contacts Api Collection Response Association Structure
  property_count: 2
  slug: crm-contacts-api-collection-response-association-structure
- name: Crm Contacts Api Collection Response Contact Structure
  property_count: 2
  slug: crm-contacts-api-collection-response-contact-structure
- name: Crm Contacts Api Contact Structure
  property_count: 6
  slug: crm-contacts-api-contact-structure
- name: Crm Contacts Api Filter Group Structure
  property_count: 1
  slug: crm-contacts-api-filter-group-structure
- name: Crm Contacts Api Filter Structure
  property_count: 3
  slug: crm-contacts-api-filter-structure
- name: Crm Contacts Api Paging Structure
  property_count: 1
  slug: crm-contacts-api-paging-structure
- name: Crm Contacts Api Search Request Structure
  property_count: 6
  slug: crm-contacts-api-search-request-structure
- name: Crm Contacts Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-contacts-api-simple-public-object-input-structure
- name: Crm Deals Api Association Structure
  property_count: 2
  slug: crm-deals-api-association-structure
- name: Crm Deals Api Batch Archive Input Structure
  property_count: 1
  slug: crm-deals-api-batch-archive-input-structure
- name: Crm Deals Api Batch Create Input Structure
  property_count: 1
  slug: crm-deals-api-batch-create-input-structure
- name: Crm Deals Api Batch Read Input Structure
  property_count: 2
  slug: crm-deals-api-batch-read-input-structure
- name: Crm Deals Api Batch Response Deal Structure
  property_count: 3
  slug: crm-deals-api-batch-response-deal-structure
- name: Crm Deals Api Batch Update Input Structure
  property_count: 1
  slug: crm-deals-api-batch-update-input-structure
- name: Crm Deals Api Collection Response Association Structure
  property_count: 2
  slug: crm-deals-api-collection-response-association-structure
- name: Crm Deals Api Collection Response Deal Structure
  property_count: 2
  slug: crm-deals-api-collection-response-deal-structure
- name: Crm Deals Api Deal Structure
  property_count: 6
  slug: crm-deals-api-deal-structure
- name: Crm Deals Api Filter Group Structure
  property_count: 1
  slug: crm-deals-api-filter-group-structure
- name: Crm Deals Api Filter Structure
  property_count: 3
  slug: crm-deals-api-filter-structure
- name: Crm Deals Api Paging Structure
  property_count: 1
  slug: crm-deals-api-paging-structure
- name: Crm Deals Api Search Request Structure
  property_count: 6
  slug: crm-deals-api-search-request-structure
- name: Crm Deals Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-deals-api-simple-public-object-input-structure
- name: Crm Feature Flags Api Batch Delete Input Item Structure
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input-item-structure
- name: Crm Feature Flags Api Batch Delete Input Structure
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input-structure
- name: Crm Feature Flags Api Batch Error Structure
  property_count: 4
  slug: crm-feature-flags-api-batch-error-structure
- name: Crm Feature Flags Api Batch Portal Flag State Input Item Structure
  property_count: 2
  slug: crm-feature-flags-api-batch-portal-flag-state-input-item-structure
- name: Crm Feature Flags Api Batch Portal Flag State Input Structure
  property_count: 1
  slug: crm-feature-flags-api-batch-portal-flag-state-input-structure
- name: Crm Feature Flags Api Batch Portal Flag State Response Structure
  property_count: 4
  slug: crm-feature-flags-api-batch-portal-flag-state-response-structure
- name: Crm Feature Flags Api Batch Portal Flag State Response With Errors Structure
  property_count: 5
  slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors-structure
- name: Crm Feature Flags Api Feature Flag Input Structure
  property_count: 1
  slug: crm-feature-flags-api-feature-flag-input-structure
- name: Crm Feature Flags Api Feature Flag Structure
  property_count: 4
  slug: crm-feature-flags-api-feature-flag-structure
- name: Crm Feature Flags Api Flag State Structure
  property_count: 0
  slug: crm-feature-flags-api-flag-state-structure
- name: Crm Feature Flags Api Paging Next Structure
  property_count: 2
  slug: crm-feature-flags-api-paging-next-structure
- name: Crm Feature Flags Api Paging Structure
  property_count: 1
  slug: crm-feature-flags-api-paging-structure
- name: Crm Feature Flags Api Portal Flag State Collection Structure
  property_count: 2
  slug: crm-feature-flags-api-portal-flag-state-collection-structure
- name: Crm Feature Flags Api Portal Flag State Input Structure
  property_count: 1
  slug: crm-feature-flags-api-portal-flag-state-input-structure
- name: Crm Feature Flags Api Portal Flag State Structure
  property_count: 4
  slug: crm-feature-flags-api-portal-flag-state-structure
- name: Crm Lists Api Collection Response List Structure
  property_count: 2
  slug: crm-lists-api-collection-response-list-structure
- name: Crm Lists Api Collection Response Membership Structure
  property_count: 2
  slug: crm-lists-api-collection-response-membership-structure
- name: Crm Lists Api List Create Request Structure
  property_count: 4
  slug: crm-lists-api-list-create-request-structure
- name: Crm Lists Api List Structure
  property_count: 9
  slug: crm-lists-api-list-structure
- name: Crm Lists Api Membership Change Request Structure
  property_count: 2
  slug: crm-lists-api-membership-change-request-structure
- name: Crm Lists Api Membership Change Response Structure
  property_count: 4
  slug: crm-lists-api-membership-change-response-structure
- name: Crm Lists Api Membership Structure
  property_count: 2
  slug: crm-lists-api-membership-structure
- name: Crm Lists Api Paging Structure
  property_count: 1
  slug: crm-lists-api-paging-structure
- name: Crm Search Api Crmobject Structure
  property_count: 5
  slug: crm-search-api-crmobject-structure
- name: Crm Search Api Filter Group Structure
  property_count: 1
  slug: crm-search-api-filter-group-structure
- name: Crm Search Api Filter Structure
  property_count: 5
  slug: crm-search-api-filter-structure
- name: Crm Search Api Paging Structure
  property_count: 1
  slug: crm-search-api-paging-structure
- name: Crm Search Api Search Request Structure
  property_count: 6
  slug: crm-search-api-search-request-structure
- name: Crm Search Api Search Response Structure
  property_count: 3
  slug: crm-search-api-search-response-structure
- name: Crm Search Api Sort Structure
  property_count: 2
  slug: crm-search-api-sort-structure
- name: Crm Tickets Api Association Structure
  property_count: 2
  slug: crm-tickets-api-association-structure
- name: Crm Tickets Api Batch Archive Input Structure
  property_count: 1
  slug: crm-tickets-api-batch-archive-input-structure
- name: Crm Tickets Api Batch Create Input Structure
  property_count: 1
  slug: crm-tickets-api-batch-create-input-structure
- name: Crm Tickets Api Batch Read Input Structure
  property_count: 2
  slug: crm-tickets-api-batch-read-input-structure
- name: Crm Tickets Api Batch Response Ticket Structure
  property_count: 3
  slug: crm-tickets-api-batch-response-ticket-structure
- name: Crm Tickets Api Batch Update Input Structure
  property_count: 1
  slug: crm-tickets-api-batch-update-input-structure
- name: Crm Tickets Api Collection Response Association Structure
  property_count: 2
  slug: crm-tickets-api-collection-response-association-structure
- name: Crm Tickets Api Collection Response Ticket Structure
  property_count: 2
  slug: crm-tickets-api-collection-response-ticket-structure
- name: Crm Tickets Api Filter Group Structure
  property_count: 1
  slug: crm-tickets-api-filter-group-structure
- name: Crm Tickets Api Filter Structure
  property_count: 3
  slug: crm-tickets-api-filter-structure
- name: Crm Tickets Api Paging Structure
  property_count: 1
  slug: crm-tickets-api-paging-structure
- name: Crm Tickets Api Search Request Structure
  property_count: 6
  slug: crm-tickets-api-search-request-structure
- name: Crm Tickets Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-tickets-api-simple-public-object-input-structure
- name: Crm Tickets Api Ticket Structure
  property_count: 6
  slug: crm-tickets-api-ticket-structure
- name: Custom Workflow Actions Api Action Definition Collection Structure
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-collection-structure
- name: Custom Workflow Actions Api Action Definition Input Structure
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-input-structure
- name: Custom Workflow Actions Api Action Definition Patch Structure
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-patch-structure
- name: Custom Workflow Actions Api Action Definition Revision Collection Structure
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-revision-collection-structure
- name: Custom Workflow Actions Api Action Definition Revision Structure
  property_count: 3
  slug: custom-workflow-actions-api-action-definition-revision-structure
- name: Custom Workflow Actions Api Action Definition Structure
  property_count: 10
  slug: custom-workflow-actions-api-action-definition-structure
- name: Custom Workflow Actions Api Action Function Collection Structure
  property_count: 1
  slug: custom-workflow-actions-api-action-function-collection-structure
- name: Custom Workflow Actions Api Action Function Input Structure
  property_count: 1
  slug: custom-workflow-actions-api-action-function-input-structure
- name: Custom Workflow Actions Api Action Function Reference Structure
  property_count: 2
  slug: custom-workflow-actions-api-action-function-reference-structure
- name: Custom Workflow Actions Api Action Function Structure
  property_count: 3
  slug: custom-workflow-actions-api-action-function-structure
- name: Custom Workflow Actions Api Action Labels Structure
  property_count: 4
  slug: custom-workflow-actions-api-action-labels-structure
- name: Custom Workflow Actions Api Batch Callback Completion Request Structure
  property_count: 1
  slug: custom-workflow-actions-api-batch-callback-completion-request-structure
- name: Custom Workflow Actions Api Batch Callback Error Structure
  property_count: 3
  slug: custom-workflow-actions-api-batch-callback-error-structure
- name: Custom Workflow Actions Api Batch Callback Input Structure
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-input-structure
- name: Custom Workflow Actions Api Batch Callback Response Structure
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-response-structure
- name: Custom Workflow Actions Api Callback Completion Request Structure
  property_count: 1
  slug: custom-workflow-actions-api-callback-completion-request-structure
- name: Custom Workflow Actions Api Field Option Structure
  property_count: 3
  slug: custom-workflow-actions-api-field-option-structure
- name: Custom Workflow Actions Api Field Type Definition Structure
  property_count: 6
  slug: custom-workflow-actions-api-field-type-definition-structure
- name: Custom Workflow Actions Api Input Field Structure
  property_count: 3
  slug: custom-workflow-actions-api-input-field-structure
- name: Custom Workflow Actions Api Object Request Options Structure
  property_count: 1
  slug: custom-workflow-actions-api-object-request-options-structure
- name: Custom Workflow Actions Api Output Field Structure
  property_count: 1
  slug: custom-workflow-actions-api-output-field-structure
- name: Custom Workflow Actions Api Paging Structure
  property_count: 1
  slug: custom-workflow-actions-api-paging-structure
- name: Domains Api Domain Collection Response Structure
  property_count: 3
  slug: domains-api-domain-collection-response-structure
- name: Domains Api Domain Structure
  property_count: 21
  slug: domains-api-domain-structure
- name: Domains Api Forward Paging Structure
  property_count: 1
  slug: domains-api-forward-paging-structure
- name: Domains Api Next Page Structure
  property_count: 2
  slug: domains-api-next-page-structure
- name: Engagement Calls Api Association Input Structure
  property_count: 2
  slug: engagement-calls-api-association-input-structure
- name: Engagement Calls Api Association Type Structure
  property_count: 2
  slug: engagement-calls-api-association-type-structure
- name: Engagement Calls Api Batch Archive Calls Request Structure
  property_count: 1
  slug: engagement-calls-api-batch-archive-calls-request-structure
- name: Engagement Calls Api Batch Calls Response Structure
  property_count: 7
  slug: engagement-calls-api-batch-calls-response-structure
- name: Engagement Calls Api Batch Create Calls Request Structure
  property_count: 1
  slug: engagement-calls-api-batch-create-calls-request-structure
- name: Engagement Calls Api Batch Error Structure
  property_count: 5
  slug: engagement-calls-api-batch-error-structure
- name: Engagement Calls Api Batch Read Calls Request Structure
  property_count: 4
  slug: engagement-calls-api-batch-read-calls-request-structure
- name: Engagement Calls Api Batch Read Input Structure
  property_count: 1
  slug: engagement-calls-api-batch-read-input-structure
- name: Engagement Calls Api Batch Update Calls Request Structure
  property_count: 1
  slug: engagement-calls-api-batch-update-calls-request-structure
- name: Engagement Calls Api Batch Update Input Structure
  property_count: 2
  slug: engagement-calls-api-batch-update-input-structure
- name: Engagement Calls Api Call Collection Response Structure
  property_count: 2
  slug: engagement-calls-api-call-collection-response-structure
- name: Engagement Calls Api Call Create Request Structure
  property_count: 2
  slug: engagement-calls-api-call-create-request-structure
- name: Engagement Calls Api Call Search Request Structure
  property_count: 6
  slug: engagement-calls-api-call-search-request-structure
- name: Engagement Calls Api Call Search Response Structure
  property_count: 3
  slug: engagement-calls-api-call-search-response-structure
- name: Engagement Calls Api Call Structure
  property_count: 7
  slug: engagement-calls-api-call-structure
- name: Engagement Calls Api Call Update Request Structure
  property_count: 1
  slug: engagement-calls-api-call-update-request-structure
- name: Engagement Calls Api Filter Group Structure
  property_count: 1
  slug: engagement-calls-api-filter-group-structure
- name: Engagement Calls Api Filter Structure
  property_count: 5
  slug: engagement-calls-api-filter-structure
- name: Engagement Calls Api Gdpr Delete Request Structure
  property_count: 2
  slug: engagement-calls-api-gdpr-delete-request-structure
- name: Engagement Calls Api Next Page Structure
  property_count: 2
  slug: engagement-calls-api-next-page-structure
- name: Engagement Calls Api Paging Structure
  property_count: 1
  slug: engagement-calls-api-paging-structure
- name: Engagement Calls Api Property History Structure
  property_count: 6
  slug: engagement-calls-api-property-history-structure
- name: Engagement Calls Api Sort Option Structure
  property_count: 2
  slug: engagement-calls-api-sort-option-structure
- name: Engagement Emails Api Association Structure
  property_count: 2
  slug: engagement-emails-api-association-structure
- name: Engagement Emails Api Batch Create Input Structure
  property_count: 1
  slug: engagement-emails-api-batch-create-input-structure
- name: Engagement Emails Api Batch Read Input Structure
  property_count: 2
  slug: engagement-emails-api-batch-read-input-structure
- name: Engagement Emails Api Batch Response Email Engagement Structure
  property_count: 3
  slug: engagement-emails-api-batch-response-email-engagement-structure
- name: Engagement Emails Api Batch Update Input Structure
  property_count: 1
  slug: engagement-emails-api-batch-update-input-structure
- name: Engagement Emails Api Collection Response Association Structure
  property_count: 2
  slug: engagement-emails-api-collection-response-association-structure
- name: Engagement Emails Api Collection Response Email Engagement Structure
  property_count: 2
  slug: engagement-emails-api-collection-response-email-engagement-structure
- name: Engagement Emails Api Email Engagement Structure
  property_count: 6
  slug: engagement-emails-api-email-engagement-structure
- name: Engagement Emails Api Filter Group Structure
  property_count: 1
  slug: engagement-emails-api-filter-group-structure
- name: Engagement Emails Api Filter Structure
  property_count: 3
  slug: engagement-emails-api-filter-structure
- name: Engagement Emails Api Paging Structure
  property_count: 1
  slug: engagement-emails-api-paging-structure
- name: Engagement Emails Api Search Request Structure
  property_count: 6
  slug: engagement-emails-api-search-request-structure
- name: Engagement Emails Api Simple Public Object Input Structure
  property_count: 1
  slug: engagement-emails-api-simple-public-object-input-structure
- name: Engagement Meetings Api Association Structure
  property_count: 2
  slug: engagement-meetings-api-association-structure
- name: Engagement Meetings Api Batch Create Input Structure
  property_count: 1
  slug: engagement-meetings-api-batch-create-input-structure
- name: Engagement Meetings Api Batch Read Input Structure
  property_count: 2
  slug: engagement-meetings-api-batch-read-input-structure
- name: Engagement Meetings Api Batch Response Meeting Structure
  property_count: 3
  slug: engagement-meetings-api-batch-response-meeting-structure
- name: Engagement Meetings Api Batch Update Input Structure
  property_count: 1
  slug: engagement-meetings-api-batch-update-input-structure
- name: Engagement Meetings Api Collection Response Association Structure
  property_count: 2
  slug: engagement-meetings-api-collection-response-association-structure
- name: Engagement Meetings Api Collection Response Meeting Structure
  property_count: 2
  slug: engagement-meetings-api-collection-response-meeting-structure
- name: Engagement Meetings Api Filter Group Structure
  property_count: 1
  slug: engagement-meetings-api-filter-group-structure
- name: Engagement Meetings Api Filter Structure
  property_count: 3
  slug: engagement-meetings-api-filter-structure
- name: Engagement Meetings Api Meeting Structure
  property_count: 6
  slug: engagement-meetings-api-meeting-structure
- name: Engagement Meetings Api Paging Structure
  property_count: 1
  slug: engagement-meetings-api-paging-structure
- name: Engagement Meetings Api Search Request Structure
  property_count: 6
  slug: engagement-meetings-api-search-request-structure
- name: Engagement Meetings Api Simple Public Object Input Structure
  property_count: 1
  slug: engagement-meetings-api-simple-public-object-input-structure
- name: Engagement Notes Association Input Structure
  property_count: 2
  slug: engagement-notes-association-input-structure
- name: Engagement Notes Association Type Structure
  property_count: 2
  slug: engagement-notes-association-type-structure
- name: Engagement Notes Batch Archive Notes Request Structure
  property_count: 1
  slug: engagement-notes-batch-archive-notes-request-structure
- name: Engagement Notes Batch Create Notes Request Structure
  property_count: 1
  slug: engagement-notes-batch-create-notes-request-structure
- name: Engagement Notes Batch Error Structure
  property_count: 5
  slug: engagement-notes-batch-error-structure
- name: Engagement Notes Batch Notes Response Structure
  property_count: 7
  slug: engagement-notes-batch-notes-response-structure
- name: Engagement Notes Batch Read Input Structure
  property_count: 1
  slug: engagement-notes-batch-read-input-structure
- name: Engagement Notes Batch Read Notes Request Structure
  property_count: 4
  slug: engagement-notes-batch-read-notes-request-structure
- name: Engagement Notes Batch Update Input Structure
  property_count: 2
  slug: engagement-notes-batch-update-input-structure
- name: Engagement Notes Batch Update Notes Request Structure
  property_count: 1
  slug: engagement-notes-batch-update-notes-request-structure
- name: Engagement Notes Filter Group Structure
  property_count: 1
  slug: engagement-notes-filter-group-structure
- name: Engagement Notes Filter Structure
  property_count: 5
  slug: engagement-notes-filter-structure
- name: Engagement Notes Gdpr Delete Request Structure
  property_count: 2
  slug: engagement-notes-gdpr-delete-request-structure
- name: Engagement Notes Next Page Structure
  property_count: 2
  slug: engagement-notes-next-page-structure
- name: Engagement Notes Note Collection Response Structure
  property_count: 2
  slug: engagement-notes-note-collection-response-structure
- name: Engagement Notes Note Create Request Structure
  property_count: 2
  slug: engagement-notes-note-create-request-structure
- name: Engagement Notes Note Search Request Structure
  property_count: 6
  slug: engagement-notes-note-search-request-structure
- name: Engagement Notes Note Search Response Structure
  property_count: 3
  slug: engagement-notes-note-search-response-structure
- name: Engagement Notes Note Structure
  property_count: 7
  slug: engagement-notes-note-structure
- name: Engagement Notes Note Update Request Structure
  property_count: 1
  slug: engagement-notes-note-update-request-structure
- name: Engagement Notes Paging Structure
  property_count: 1
  slug: engagement-notes-paging-structure
- name: Engagement Notes Property History Structure
  property_count: 6
  slug: engagement-notes-property-history-structure
- name: Engagement Notes Sort Option Structure
  property_count: 2
  slug: engagement-notes-sort-option-structure
- name: Engagement Tasks Api Association Structure
  property_count: 2
  slug: engagement-tasks-api-association-structure
- name: Engagement Tasks Api Batch Create Input Structure
  property_count: 1
  slug: engagement-tasks-api-batch-create-input-structure
- name: Engagement Tasks Api Batch Read Input Structure
  property_count: 2
  slug: engagement-tasks-api-batch-read-input-structure
- name: Engagement Tasks Api Batch Response Task Structure
  property_count: 3
  slug: engagement-tasks-api-batch-response-task-structure
- name: Engagement Tasks Api Batch Update Input Structure
  property_count: 1
  slug: engagement-tasks-api-batch-update-input-structure
- name: Engagement Tasks Api Collection Response Association Structure
  property_count: 2
  slug: engagement-tasks-api-collection-response-association-structure
- name: Engagement Tasks Api Collection Response Task Structure
  property_count: 2
  slug: engagement-tasks-api-collection-response-task-structure
- name: Engagement Tasks Api Filter Group Structure
  property_count: 1
  slug: engagement-tasks-api-filter-group-structure
- name: Engagement Tasks Api Filter Structure
  property_count: 3
  slug: engagement-tasks-api-filter-structure
- name: Engagement Tasks Api Paging Structure
  property_count: 1
  slug: engagement-tasks-api-paging-structure
- name: Engagement Tasks Api Search Request Structure
  property_count: 6
  slug: engagement-tasks-api-search-request-structure
- name: Engagement Tasks Api Simple Public Object Input Structure
  property_count: 1
  slug: engagement-tasks-api-simple-public-object-input-structure
- name: Engagement Tasks Api Task Structure
  property_count: 6
  slug: engagement-tasks-api-task-structure
- name: Hubspot Analytics Events Error Detail Structure
  property_count: 5
  slug: hubspot-analytics-events-error-detail-structure
- name: Hubspot Analytics Events Error Structure
  property_count: 7
  slug: hubspot-analytics-events-error-structure
- name: Hubspot Analytics Events Event Instance Collection Structure
  property_count: 2
  slug: hubspot-analytics-events-event-instance-collection-structure
- name: Hubspot Analytics Events Event Instance Structure
  property_count: 6
  slug: hubspot-analytics-events-event-instance-structure
- name: Hubspot Analytics Events Event Type Collection Structure
  property_count: 1
  slug: hubspot-analytics-events-event-type-collection-structure
- name: Hubspot Analytics Events Paging Next Structure
  property_count: 2
  slug: hubspot-analytics-events-paging-next-structure
- name: Hubspot Analytics Events Paging Previous Structure
  property_count: 2
  slug: hubspot-analytics-events-paging-previous-structure
- name: Hubspot Analytics Events Paging Structure
  property_count: 2
  slug: hubspot-analytics-events-paging-structure
- name: Hubspot Authors Attach To Language Group Request Structure
  property_count: 4
  slug: hubspot-authors-attach-to-language-group-request-structure
- name: Hubspot Authors Batch Archive Input Structure
  property_count: 1
  slug: hubspot-authors-batch-archive-input-structure
- name: Hubspot Authors Batch Create Input Structure
  property_count: 1
  slug: hubspot-authors-batch-create-input-structure
- name: Hubspot Authors Batch Input Item Structure
  property_count: 2
  slug: hubspot-authors-batch-input-item-structure
- name: Hubspot Authors Batch Input Structure
  property_count: 1
  slug: hubspot-authors-batch-input-structure
- name: Hubspot Authors Batch Read Input Structure
  property_count: 1
  slug: hubspot-authors-batch-read-input-structure
- name: Hubspot Authors Batch Response Structure
  property_count: 6
  slug: hubspot-authors-batch-response-structure
- name: Hubspot Authors Batch Response With Errors Structure
  property_count: 0
  slug: hubspot-authors-batch-response-with-errors-structure
- name: Hubspot Authors Blog Author Collection Structure
  property_count: 3
  slug: hubspot-authors-blog-author-collection-structure
- name: Hubspot Authors Blog Author Input Structure
  property_count: 9
  slug: hubspot-authors-blog-author-input-structure
- name: Hubspot Authors Blog Author Structure
  property_count: 15
  slug: hubspot-authors-blog-author-structure
- name: Hubspot Authors Create Language Variation Request Structure
  property_count: 2
  slug: hubspot-authors-create-language-variation-request-structure
- name: Hubspot Authors Detach From Language Group Request Structure
  property_count: 1
  slug: hubspot-authors-detach-from-language-group-request-structure
- name: Hubspot Authors Error Detail Structure
  property_count: 5
  slug: hubspot-authors-error-detail-structure
- name: Hubspot Authors Error Structure
  property_count: 7
  slug: hubspot-authors-error-structure
- name: Hubspot Authors Paging Next Structure
  property_count: 2
  slug: hubspot-authors-paging-next-structure
- name: Hubspot Authors Paging Structure
  property_count: 1
  slug: hubspot-authors-paging-structure
- name: Hubspot Authors Set Language Primary Request Structure
  property_count: 1
  slug: hubspot-authors-set-language-primary-request-structure
- name: Hubspot Authors Standard Error Structure
  property_count: 7
  slug: hubspot-authors-standard-error-structure
- name: Hubspot Blog Posts Attach To Language Group Request Structure
  property_count: 4
  slug: hubspot-blog-posts-attach-to-language-group-request-structure
- name: Hubspot Blog Posts Batch Input Item Structure
  property_count: 1
  slug: hubspot-blog-posts-batch-input-item-structure
- name: Hubspot Blog Posts Batch Input Structure
  property_count: 1
  slug: hubspot-blog-posts-batch-input-structure
- name: Hubspot Blog Posts Batch Response Structure
  property_count: 6
  slug: hubspot-blog-posts-batch-response-structure
- name: Hubspot Blog Posts Batch Response With Errors Structure
  property_count: 0
  slug: hubspot-blog-posts-batch-response-with-errors-structure
- name: Hubspot Blog Posts Blog Post Collection Structure
  property_count: 3
  slug: hubspot-blog-posts-blog-post-collection-structure
- name: Hubspot Blog Posts Blog Post Input Structure
  property_count: 15
  slug: hubspot-blog-posts-blog-post-input-structure
- name: Hubspot Blog Posts Blog Post Structure
  property_count: 32
  slug: hubspot-blog-posts-blog-post-structure
- name: Hubspot Blog Posts Clone Request Structure
  property_count: 1
  slug: hubspot-blog-posts-clone-request-structure
- name: Hubspot Blog Posts Create Language Variation Request Structure
  property_count: 2
  slug: hubspot-blog-posts-create-language-variation-request-structure
- name: Hubspot Blog Posts Detach From Language Group Request Structure
  property_count: 1
  slug: hubspot-blog-posts-detach-from-language-group-request-structure
- name: Hubspot Blog Posts Error Detail Structure
  property_count: 5
  slug: hubspot-blog-posts-error-detail-structure
- name: Hubspot Blog Posts Error Structure
  property_count: 7
  slug: hubspot-blog-posts-error-structure
- name: Hubspot Blog Posts Paging Next Structure
  property_count: 2
  slug: hubspot-blog-posts-paging-next-structure
- name: Hubspot Blog Posts Paging Previous Structure
  property_count: 2
  slug: hubspot-blog-posts-paging-previous-structure
- name: Hubspot Blog Posts Paging Structure
  property_count: 2
  slug: hubspot-blog-posts-paging-structure
- name: Hubspot Blog Posts Push Live Request Structure
  property_count: 1
  slug: hubspot-blog-posts-push-live-request-structure
- name: Hubspot Blog Posts Reset Draft Request Structure
  property_count: 1
  slug: hubspot-blog-posts-reset-draft-request-structure
- name: Hubspot Blog Posts Restore Previous Version Request Structure
  property_count: 2
  slug: hubspot-blog-posts-restore-previous-version-request-structure
- name: Hubspot Blog Posts Schedule Request Structure
  property_count: 2
  slug: hubspot-blog-posts-schedule-request-structure
- name: Hubspot Blog Posts Set Language Primary Request Structure
  property_count: 1
  slug: hubspot-blog-posts-set-language-primary-request-structure
- name: Hubspot Blog Posts Standard Error Structure
  property_count: 7
  slug: hubspot-blog-posts-standard-error-structure
- name: Hubspot Blog Posts Version History Structure
  property_count: 4
  slug: hubspot-blog-posts-version-history-structure
- name: Hubspot Cms Hubdb Collection Response Hub Db Row Structure
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-row-structure
- name: Hubspot Cms Hubdb Collection Response Hub Db Table Structure
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-table-structure
- name: Hubspot Cms Hubdb Error Structure
  property_count: 4
  slug: hubspot-cms-hubdb-error-structure
- name: Hubspot Cms Hubdb Hub Db Column Structure
  property_count: 5
  slug: hubspot-cms-hubdb-hub-db-column-structure
- name: Hubspot Cms Hubdb Hub Db Row Create Request Structure
  property_count: 1
  slug: hubspot-cms-hubdb-hub-db-row-create-request-structure
- name: Hubspot Cms Hubdb Hub Db Row Structure
  property_count: 4
  slug: hubspot-cms-hubdb-hub-db-row-structure
- name: Hubspot Cms Hubdb Hub Db Table Create Request Structure
  property_count: 3
  slug: hubspot-cms-hubdb-hub-db-table-create-request-structure
- name: Hubspot Cms Hubdb Hub Db Table Structure
  property_count: 9
  slug: hubspot-cms-hubdb-hub-db-table-structure
- name: Hubspot Cms Hubdb Paging Structure
  property_count: 1
  slug: hubspot-cms-hubdb-paging-structure
- name: Hubspot Cms Pages Collection Response Page Structure
  property_count: 2
  slug: hubspot-cms-pages-collection-response-page-structure
- name: Hubspot Cms Pages Error Structure
  property_count: 4
  slug: hubspot-cms-pages-error-structure
- name: Hubspot Cms Pages Page Create Request Structure
  property_count: 8
  slug: hubspot-cms-pages-page-create-request-structure
- name: Hubspot Cms Pages Page Structure
  property_count: 16
  slug: hubspot-cms-pages-page-structure
- name: Hubspot Cms Pages Page Update Request Structure
  property_count: 5
  slug: hubspot-cms-pages-page-update-request-structure
- name: Hubspot Cms Pages Paging Structure
  property_count: 1
  slug: hubspot-cms-pages-paging-structure
- name: Hubspot Commerce Payments Association Input Structure
  property_count: 2
  slug: hubspot-commerce-payments-association-input-structure
- name: Hubspot Commerce Payments Association Result Structure
  property_count: 2
  slug: hubspot-commerce-payments-association-result-structure
- name: Hubspot Commerce Payments Association Type Structure
  property_count: 2
  slug: hubspot-commerce-payments-association-type-structure
- name: Hubspot Commerce Payments Batch Archive Request Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-archive-request-structure
- name: Hubspot Commerce Payments Batch Create Request Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-create-request-structure
- name: Hubspot Commerce Payments Batch Create Response Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-create-response-structure
- name: Hubspot Commerce Payments Batch Error Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-error-structure
- name: Hubspot Commerce Payments Batch Read Input Item Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-read-input-item-structure
- name: Hubspot Commerce Payments Batch Read Request Structure
  property_count: 4
  slug: hubspot-commerce-payments-batch-read-request-structure
- name: Hubspot Commerce Payments Batch Read Response Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-read-response-structure
- name: Hubspot Commerce Payments Batch Update Input Item Structure
  property_count: 3
  slug: hubspot-commerce-payments-batch-update-input-item-structure
- name: Hubspot Commerce Payments Batch Update Request Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-update-request-structure
- name: Hubspot Commerce Payments Batch Update Response Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-update-response-structure
- name: Hubspot Commerce Payments Commerce Payment Collection Structure
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-collection-structure
- name: Hubspot Commerce Payments Commerce Payment Input Structure
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-input-structure
- name: Hubspot Commerce Payments Commerce Payment Patch Structure
  property_count: 1
  slug: hubspot-commerce-payments-commerce-payment-patch-structure
- name: Hubspot Commerce Payments Commerce Payment Structure
  property_count: 8
  slug: hubspot-commerce-payments-commerce-payment-structure
- name: Hubspot Commerce Payments Error Detail Structure
  property_count: 5
  slug: hubspot-commerce-payments-error-detail-structure
- name: Hubspot Commerce Payments Error Structure
  property_count: 7
  slug: hubspot-commerce-payments-error-structure
- name: Hubspot Commerce Payments Filter Group Structure
  property_count: 1
  slug: hubspot-commerce-payments-filter-group-structure
- name: Hubspot Commerce Payments Filter Structure
  property_count: 5
  slug: hubspot-commerce-payments-filter-structure
- name: Hubspot Commerce Payments Paging Structure
  property_count: 2
  slug: hubspot-commerce-payments-paging-structure
- name: Hubspot Commerce Payments Property History Structure
  property_count: 6
  slug: hubspot-commerce-payments-property-history-structure
- name: Hubspot Commerce Payments Search Request Structure
  property_count: 6
  slug: hubspot-commerce-payments-search-request-structure
- name: Hubspot Commerce Payments Search Response Structure
  property_count: 3
  slug: hubspot-commerce-payments-search-response-structure
- name: Hubspot Commerce Payments Sort Option Structure
  property_count: 2
  slug: hubspot-commerce-payments-sort-option-structure
- name: Hubspot Commerce Subscriptions Association Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-association-structure
- name: Hubspot Commerce Subscriptions Batch Create Input Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-create-input-structure
- name: Hubspot Commerce Subscriptions Batch Read Input Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-batch-read-input-structure
- name: Hubspot Commerce Subscriptions Batch Response Subscription Structure
  property_count: 3
  slug: hubspot-commerce-subscriptions-batch-response-subscription-structure
- name: Hubspot Commerce Subscriptions Batch Update Input Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-update-input-structure
- name: Hubspot Commerce Subscriptions Collection Response Association Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-association-structure
- name: Hubspot Commerce Subscriptions Collection Response Subscription Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-subscription-structure
- name: Hubspot Commerce Subscriptions Error Structure
  property_count: 4
  slug: hubspot-commerce-subscriptions-error-structure
- name: Hubspot Commerce Subscriptions Filter Group Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-filter-group-structure
- name: Hubspot Commerce Subscriptions Filter Structure
  property_count: 3
  slug: hubspot-commerce-subscriptions-filter-structure
- name: Hubspot Commerce Subscriptions Paging Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-paging-structure
- name: Hubspot Commerce Subscriptions Search Request Structure
  property_count: 6
  slug: hubspot-commerce-subscriptions-search-request-structure
- name: Hubspot Commerce Subscriptions Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-simple-public-object-input-structure
- name: Hubspot Commerce Subscriptions Subscription Structure
  property_count: 6
  slug: hubspot-commerce-subscriptions-subscription-structure
- name: Hubspot Conversations Actor Collection Structure
  property_count: 2
  slug: hubspot-conversations-actor-collection-structure
- name: Hubspot Conversations Actor Structure
  property_count: 5
  slug: hubspot-conversations-actor-structure
- name: Hubspot Conversations Attachment Structure
  property_count: 5
  slug: hubspot-conversations-attachment-structure
- name: Hubspot Conversations Channel Collection Structure
  property_count: 2
  slug: hubspot-conversations-channel-collection-structure
- name: Hubspot Conversations Channel Structure
  property_count: 5
  slug: hubspot-conversations-channel-structure
- name: Hubspot Conversations Error Detail Structure
  property_count: 5
  slug: hubspot-conversations-error-detail-structure
- name: Hubspot Conversations Error Structure
  property_count: 7
  slug: hubspot-conversations-error-structure
- name: Hubspot Conversations Inbox Collection Structure
  property_count: 3
  slug: hubspot-conversations-inbox-collection-structure
- name: Hubspot Conversations Inbox Structure
  property_count: 6
  slug: hubspot-conversations-inbox-structure
- name: Hubspot Conversations Message Collection Structure
  property_count: 2
  slug: hubspot-conversations-message-collection-structure
- name: Hubspot Conversations Message Recipient Structure
  property_count: 1
  slug: hubspot-conversations-message-recipient-structure
- name: Hubspot Conversations Message Status Structure
  property_count: 1
  slug: hubspot-conversations-message-status-structure
- name: Hubspot Conversations Message Structure
  property_count: 13
  slug: hubspot-conversations-message-structure
- name: Hubspot Conversations Paging Next Structure
  property_count: 2
  slug: hubspot-conversations-paging-next-structure
- name: Hubspot Conversations Paging Structure
  property_count: 1
  slug: hubspot-conversations-paging-structure
- name: Hubspot Conversations Send Message Request Structure
  property_count: 7
  slug: hubspot-conversations-send-message-request-structure
- name: Hubspot Conversations Thread Collection Structure
  property_count: 2
  slug: hubspot-conversations-thread-collection-structure
- name: Hubspot Conversations Thread Structure
  property_count: 14
  slug: hubspot-conversations-thread-structure
- name: Hubspot Conversations Update Thread Request Structure
  property_count: 2
  slug: hubspot-conversations-update-thread-request-structure
- name: Hubspot Crm Associations Association Definition Collection Structure
  property_count: 2
  slug: hubspot-crm-associations-association-definition-collection-structure
- name: Hubspot Crm Associations Association Definition Structure
  property_count: 7
  slug: hubspot-crm-associations-association-definition-structure
- name: Hubspot Crm Associations Association Label Collection Structure
  property_count: 2
  slug: hubspot-crm-associations-association-label-collection-structure
- name: Hubspot Crm Associations Association Label Structure
  property_count: 3
  slug: hubspot-crm-associations-association-label-structure
- name: Hubspot Crm Associations Association Result Structure
  property_count: 3
  slug: hubspot-crm-associations-association-result-structure
- name: Hubspot Crm Associations Association Structure
  property_count: 2
  slug: hubspot-crm-associations-association-structure
- name: Hubspot Crm Associations Association Type Input Structure
  property_count: 2
  slug: hubspot-crm-associations-association-type-input-structure
- name: Hubspot Crm Associations Association Type Structure
  property_count: 3
  slug: hubspot-crm-associations-association-type-structure
- name: Hubspot Crm Associations Batch Association Archive Input Structure
  property_count: 1
  slug: hubspot-crm-associations-batch-association-archive-input-structure
- name: Hubspot Crm Associations Batch Association Archive Item Structure
  property_count: 3
  slug: hubspot-crm-associations-batch-association-archive-item-structure
- name: Hubspot Crm Associations Batch Association Create Input Structure
  property_count: 1
  slug: hubspot-crm-associations-batch-association-create-input-structure
- name: Hubspot Crm Associations Batch Association Create Item Structure
  property_count: 3
  slug: hubspot-crm-associations-batch-association-create-item-structure
- name: Hubspot Crm Associations Batch Association Read Input Structure
  property_count: 1
  slug: hubspot-crm-associations-batch-association-read-input-structure
- name: Hubspot Crm Associations Batch Association Response Structure
  property_count: 8
  slug: hubspot-crm-associations-batch-association-response-structure
- name: Hubspot Crm Associations Create Association Input Structure
  property_count: 2
  slug: hubspot-crm-associations-create-association-input-structure
- name: Hubspot Crm Associations Create Label Input Structure
  property_count: 3
  slug: hubspot-crm-associations-create-label-input-structure
- name: Hubspot Crm Associations Error Detail Structure
  property_count: 5
  slug: hubspot-crm-associations-error-detail-structure
- name: Hubspot Crm Associations Error Structure
  property_count: 7
  slug: hubspot-crm-associations-error-structure
- name: Hubspot Crm Associations Object Reference Structure
  property_count: 1
  slug: hubspot-crm-associations-object-reference-structure
- name: Hubspot Crm Associations Paging Next Structure
  property_count: 2
  slug: hubspot-crm-associations-paging-next-structure
- name: Hubspot Crm Associations Paging Structure
  property_count: 1
  slug: hubspot-crm-associations-paging-structure
- name: Hubspot Crm Associations Standard Error Structure
  property_count: 7
  slug: hubspot-crm-associations-standard-error-structure
- name: Hubspot Crm Companies Association Structure
  property_count: 2
  slug: hubspot-crm-companies-association-structure
- name: Hubspot Crm Companies Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-companies-batch-archive-input-structure
- name: Hubspot Crm Companies Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-companies-batch-create-input-structure
- name: Hubspot Crm Companies Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-companies-batch-read-input-structure
- name: Hubspot Crm Companies Batch Response Company Structure
  property_count: 3
  slug: hubspot-crm-companies-batch-response-company-structure
- name: Hubspot Crm Companies Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-companies-batch-update-input-structure
- name: Hubspot Crm Companies Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-companies-collection-response-association-structure
- name: Hubspot Crm Companies Collection Response Company Structure
  property_count: 2
  slug: hubspot-crm-companies-collection-response-company-structure
- name: Hubspot Crm Companies Company Structure
  property_count: 6
  slug: hubspot-crm-companies-company-structure
- name: Hubspot Crm Companies Error Structure
  property_count: 4
  slug: hubspot-crm-companies-error-structure
- name: Hubspot Crm Companies Filter Group Structure
  property_count: 1
  slug: hubspot-crm-companies-filter-group-structure
- name: Hubspot Crm Companies Filter Structure
  property_count: 3
  slug: hubspot-crm-companies-filter-structure
- name: Hubspot Crm Companies Paging Structure
  property_count: 1
  slug: hubspot-crm-companies-paging-structure
- name: Hubspot Crm Companies Search Request Structure
  property_count: 6
  slug: hubspot-crm-companies-search-request-structure
- name: Hubspot Crm Companies Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-companies-simple-public-object-input-structure
- name: Hubspot Crm Contacts Association Structure
  property_count: 2
  slug: hubspot-crm-contacts-association-structure
- name: Hubspot Crm Contacts Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-batch-archive-input-structure
- name: Hubspot Crm Contacts Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-batch-create-input-structure
- name: Hubspot Crm Contacts Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-contacts-batch-read-input-structure
- name: Hubspot Crm Contacts Batch Response Contact Structure
  property_count: 3
  slug: hubspot-crm-contacts-batch-response-contact-structure
- name: Hubspot Crm Contacts Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-batch-update-input-structure
- name: Hubspot Crm Contacts Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-association-structure
- name: Hubspot Crm Contacts Collection Response Contact Structure
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-contact-structure
- name: Hubspot Crm Contacts Contact Structure
  property_count: 6
  slug: hubspot-crm-contacts-contact-structure
- name: Hubspot Crm Contacts Error Structure
  property_count: 4
  slug: hubspot-crm-contacts-error-structure
- name: Hubspot Crm Contacts Filter Group Structure
  property_count: 1
  slug: hubspot-crm-contacts-filter-group-structure
- name: Hubspot Crm Contacts Filter Structure
  property_count: 3
  slug: hubspot-crm-contacts-filter-structure
- name: Hubspot Crm Contacts Paging Structure
  property_count: 1
  slug: hubspot-crm-contacts-paging-structure
- name: Hubspot Crm Contacts Search Request Structure
  property_count: 6
  slug: hubspot-crm-contacts-search-request-structure
- name: Hubspot Crm Contacts Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-simple-public-object-input-structure
- name: Hubspot Crm Deals Association Structure
  property_count: 2
  slug: hubspot-crm-deals-association-structure
- name: Hubspot Crm Deals Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-deals-batch-archive-input-structure
- name: Hubspot Crm Deals Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-deals-batch-create-input-structure
- name: Hubspot Crm Deals Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-deals-batch-read-input-structure
- name: Hubspot Crm Deals Batch Response Deal Structure
  property_count: 3
  slug: hubspot-crm-deals-batch-response-deal-structure
- name: Hubspot Crm Deals Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-deals-batch-update-input-structure
- name: Hubspot Crm Deals Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-deals-collection-response-association-structure
- name: Hubspot Crm Deals Collection Response Deal Structure
  property_count: 2
  slug: hubspot-crm-deals-collection-response-deal-structure
- name: Hubspot Crm Deals Deal Structure
  property_count: 6
  slug: hubspot-crm-deals-deal-structure
- name: Hubspot Crm Deals Error Structure
  property_count: 4
  slug: hubspot-crm-deals-error-structure
- name: Hubspot Crm Deals Filter Group Structure
  property_count: 1
  slug: hubspot-crm-deals-filter-group-structure
- name: Hubspot Crm Deals Filter Structure
  property_count: 3
  slug: hubspot-crm-deals-filter-structure
- name: Hubspot Crm Deals Paging Structure
  property_count: 1
  slug: hubspot-crm-deals-paging-structure
- name: Hubspot Crm Deals Search Request Structure
  property_count: 6
  slug: hubspot-crm-deals-search-request-structure
- name: Hubspot Crm Deals Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-deals-simple-public-object-input-structure
- name: Hubspot Crm Feature Flags Batch Delete Input Item Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input-item-structure
- name: Hubspot Crm Feature Flags Batch Delete Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input-structure
- name: Hubspot Crm Feature Flags Batch Error Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-error-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Input Item Structure
  property_count: 2
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-item-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Response Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Response With Errors Structure
  property_count: 5
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-with-errors-structure
- name: Hubspot Crm Feature Flags Error Detail Structure
  property_count: 5
  slug: hubspot-crm-feature-flags-error-detail-structure
- name: Hubspot Crm Feature Flags Error Structure
  property_count: 7
  slug: hubspot-crm-feature-flags-error-structure
- name: Hubspot Crm Feature Flags Feature Flag Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-feature-flag-input-structure
- name: Hubspot Crm Feature Flags Feature Flag Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-feature-flag-structure
- name: Hubspot Crm Feature Flags Flag State Structure
  property_count: 0
  slug: hubspot-crm-feature-flags-flag-state-structure
- name: Hubspot Crm Feature Flags Paging Next Structure
  property_count: 2
  slug: hubspot-crm-feature-flags-paging-next-structure
- name: Hubspot Crm Feature Flags Paging Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-paging-structure
- name: Hubspot Crm Feature Flags Portal Flag State Collection Structure
  property_count: 2
  slug: hubspot-crm-feature-flags-portal-flag-state-collection-structure
- name: Hubspot Crm Feature Flags Portal Flag State Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-portal-flag-state-input-structure
- name: Hubspot Crm Feature Flags Portal Flag State Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-portal-flag-state-structure
- name: Hubspot Crm Lists Collection Response List Structure
  property_count: 2
  slug: hubspot-crm-lists-collection-response-list-structure
- name: Hubspot Crm Lists Collection Response Membership Structure
  property_count: 2
  slug: hubspot-crm-lists-collection-response-membership-structure
- name: Hubspot Crm Lists Error Structure
  property_count: 4
  slug: hubspot-crm-lists-error-structure
- name: Hubspot Crm Lists List Create Request Structure
  property_count: 4
  slug: hubspot-crm-lists-list-create-request-structure
- name: Hubspot Crm Lists List Structure
  property_count: 9
  slug: hubspot-crm-lists-list-structure
- name: Hubspot Crm Lists Membership Change Request Structure
  property_count: 2
  slug: hubspot-crm-lists-membership-change-request-structure
- name: Hubspot Crm Lists Membership Change Response Structure
  property_count: 4
  slug: hubspot-crm-lists-membership-change-response-structure
- name: Hubspot Crm Lists Membership Structure
  property_count: 2
  slug: hubspot-crm-lists-membership-structure
- name: Hubspot Crm Lists Paging Structure
  property_count: 1
  slug: hubspot-crm-lists-paging-structure
- name: Hubspot Crm Search Crm Object Structure
  property_count: 5
  slug: hubspot-crm-search-crm-object-structure
- name: Hubspot Crm Search Error Structure
  property_count: 5
  slug: hubspot-crm-search-error-structure
- name: Hubspot Crm Search Filter Group Structure
  property_count: 1
  slug: hubspot-crm-search-filter-group-structure
- name: Hubspot Crm Search Filter Structure
  property_count: 5
  slug: hubspot-crm-search-filter-structure
- name: Hubspot Crm Search Paging Structure
  property_count: 1
  slug: hubspot-crm-search-paging-structure
- name: Hubspot Crm Search Search Request Structure
  property_count: 6
  slug: hubspot-crm-search-search-request-structure
- name: Hubspot Crm Search Search Response Structure
  property_count: 3
  slug: hubspot-crm-search-search-response-structure
- name: Hubspot Crm Search Sort Structure
  property_count: 2
  slug: hubspot-crm-search-sort-structure
- name: Hubspot Crm Tickets Association Structure
  property_count: 2
  slug: hubspot-crm-tickets-association-structure
- name: Hubspot Crm Tickets Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-batch-archive-input-structure
- name: Hubspot Crm Tickets Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-batch-create-input-structure
- name: Hubspot Crm Tickets Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-tickets-batch-read-input-structure
- name: Hubspot Crm Tickets Batch Response Ticket Structure
  property_count: 3
  slug: hubspot-crm-tickets-batch-response-ticket-structure
- name: Hubspot Crm Tickets Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-batch-update-input-structure
- name: Hubspot Crm Tickets Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-association-structure
- name: Hubspot Crm Tickets Collection Response Ticket Structure
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-ticket-structure
- name: Hubspot Crm Tickets Error Structure
  property_count: 4
  slug: hubspot-crm-tickets-error-structure
- name: Hubspot Crm Tickets Filter Group Structure
  property_count: 1
  slug: hubspot-crm-tickets-filter-group-structure
- name: Hubspot Crm Tickets Filter Structure
  property_count: 3
  slug: hubspot-crm-tickets-filter-structure
- name: Hubspot Crm Tickets Paging Structure
  property_count: 1
  slug: hubspot-crm-tickets-paging-structure
- name: Hubspot Crm Tickets Search Request Structure
  property_count: 6
  slug: hubspot-crm-tickets-search-request-structure
- name: Hubspot Crm Tickets Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-simple-public-object-input-structure
- name: Hubspot Crm Tickets Ticket Structure
  property_count: 6
  slug: hubspot-crm-tickets-ticket-structure
- name: Hubspot Custom Workflow Actions Action Definition Collection Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-collection-structure
- name: Hubspot Custom Workflow Actions Action Definition Input Structure
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-input-structure
- name: Hubspot Custom Workflow Actions Action Definition Patch Structure
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-patch-structure
- name: Hubspot Custom Workflow Actions Action Definition Revision Collection Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-revision-collection-structure
- name: Hubspot Custom Workflow Actions Action Definition Revision Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-definition-revision-structure
- name: Hubspot Custom Workflow Actions Action Definition Structure
  property_count: 10
  slug: hubspot-custom-workflow-actions-action-definition-structure
- name: Hubspot Custom Workflow Actions Action Function Collection Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-collection-structure
- name: Hubspot Custom Workflow Actions Action Function Input Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-input-structure
- name: Hubspot Custom Workflow Actions Action Function Reference Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-function-reference-structure
- name: Hubspot Custom Workflow Actions Action Function Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-function-structure
- name: Hubspot Custom Workflow Actions Action Labels Structure
  property_count: 4
  slug: hubspot-custom-workflow-actions-action-labels-structure
- name: Hubspot Custom Workflow Actions Batch Callback Completion Request Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-batch-callback-completion-request-structure
- name: Hubspot Custom Workflow Actions Batch Callback Error Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-batch-callback-error-structure
- name: Hubspot Custom Workflow Actions Batch Callback Input Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-input-structure
- name: Hubspot Custom Workflow Actions Batch Callback Response Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-response-structure
- name: Hubspot Custom Workflow Actions Callback Completion Request Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-callback-completion-request-structure
- name: Hubspot Custom Workflow Actions Error Detail Structure
  property_count: 5
  slug: hubspot-custom-workflow-actions-error-detail-structure
- name: Hubspot Custom Workflow Actions Error Structure
  property_count: 7
  slug: hubspot-custom-workflow-actions-error-structure
- name: Hubspot Custom Workflow Actions Field Option Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-field-option-structure
- name: Hubspot Custom Workflow Actions Field Type Definition Structure
  property_count: 6
  slug: hubspot-custom-workflow-actions-field-type-definition-structure
- name: Hubspot Custom Workflow Actions Input Field Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-input-field-structure
- name: Hubspot Custom Workflow Actions Object Request Options Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-object-request-options-structure
- name: Hubspot Custom Workflow Actions Output Field Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-output-field-structure
- name: Hubspot Custom Workflow Actions Paging Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-paging-structure
- name: Hubspot Domains Domain Collection Response Structure
  property_count: 3
  slug: hubspot-domains-domain-collection-response-structure
- name: Hubspot Domains Domain Structure
  property_count: 21
  slug: hubspot-domains-domain-structure
- name: Hubspot Domains Error Detail Structure
  property_count: 5
  slug: hubspot-domains-error-detail-structure
- name: Hubspot Domains Error Structure
  property_count: 7
  slug: hubspot-domains-error-structure
- name: Hubspot Domains Forward Paging Structure
  property_count: 1
  slug: hubspot-domains-forward-paging-structure
- name: Hubspot Domains Next Page Structure
  property_count: 2
  slug: hubspot-domains-next-page-structure
- name: Hubspot Engagement Calls Association Input Structure
  property_count: 2
  slug: hubspot-engagement-calls-association-input-structure
- name: Hubspot Engagement Calls Association Type Structure
  property_count: 2
  slug: hubspot-engagement-calls-association-type-structure
- name: Hubspot Engagement Calls Batch Archive Calls Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-archive-calls-request-structure
- name: Hubspot Engagement Calls Batch Calls Response Structure
  property_count: 7
  slug: hubspot-engagement-calls-batch-calls-response-structure
- name: Hubspot Engagement Calls Batch Create Calls Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-create-calls-request-structure
- name: Hubspot Engagement Calls Batch Error Structure
  property_count: 5
  slug: hubspot-engagement-calls-batch-error-structure
- name: Hubspot Engagement Calls Batch Read Calls Request Structure
  property_count: 4
  slug: hubspot-engagement-calls-batch-read-calls-request-structure
- name: Hubspot Engagement Calls Batch Read Input Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-read-input-structure
- name: Hubspot Engagement Calls Batch Update Calls Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-update-calls-request-structure
- name: Hubspot Engagement Calls Batch Update Input Structure
  property_count: 2
  slug: hubspot-engagement-calls-batch-update-input-structure
- name: Hubspot Engagement Calls Call Collection Response Structure
  property_count: 2
  slug: hubspot-engagement-calls-call-collection-response-structure
- name: Hubspot Engagement Calls Call Create Request Structure
  property_count: 2
  slug: hubspot-engagement-calls-call-create-request-structure
- name: Hubspot Engagement Calls Call Search Request Structure
  property_count: 6
  slug: hubspot-engagement-calls-call-search-request-structure
- name: Hubspot Engagement Calls Call Search Response Structure
  property_count: 3
  slug: hubspot-engagement-calls-call-search-response-structure
- name: Hubspot Engagement Calls Call Structure
  property_count: 7
  slug: hubspot-engagement-calls-call-structure
- name: Hubspot Engagement Calls Call Update Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-call-update-request-structure
- name: Hubspot Engagement Calls Error Detail Structure
  property_count: 5
  slug: hubspot-engagement-calls-error-detail-structure
- name: Hubspot Engagement Calls Error Structure
  property_count: 7
  slug: hubspot-engagement-calls-error-structure
- name: Hubspot Engagement Calls Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-calls-filter-group-structure
- name: Hubspot Engagement Calls Filter Structure
  property_count: 5
  slug: hubspot-engagement-calls-filter-structure
- name: Hubspot Engagement Calls Gdpr Delete Request Structure
  property_count: 2
  slug: hubspot-engagement-calls-gdpr-delete-request-structure
- name: Hubspot Engagement Calls Next Page Structure
  property_count: 2
  slug: hubspot-engagement-calls-next-page-structure
- name: Hubspot Engagement Calls Paging Structure
  property_count: 1
  slug: hubspot-engagement-calls-paging-structure
- name: Hubspot Engagement Calls Property History Structure
  property_count: 6
  slug: hubspot-engagement-calls-property-history-structure
- name: Hubspot Engagement Calls Sort Option Structure
  property_count: 2
  slug: hubspot-engagement-calls-sort-option-structure
- name: Hubspot Engagement Emails Association Structure
  property_count: 2
  slug: hubspot-engagement-emails-association-structure
- name: Hubspot Engagement Emails Batch Create Input Structure
  property_count: 1
  slug: hubspot-engagement-emails-batch-create-input-structure
- name: Hubspot Engagement Emails Batch Read Input Structure
  property_count: 2
  slug: hubspot-engagement-emails-batch-read-input-structure
- name: Hubspot Engagement Emails Batch Response Email Engagement Structure
  property_count: 3
  slug: hubspot-engagement-emails-batch-response-email-engagement-structure
- name: Hubspot Engagement Emails Batch Update Input Structure
  property_count: 1
  slug: hubspot-engagement-emails-batch-update-input-structure
- name: Hubspot Engagement Emails Collection Response Association Structure
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-association-structure
- name: Hubspot Engagement Emails Collection Response Email Engagement Structure
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-email-engagement-structure
- name: Hubspot Engagement Emails Email Engagement Structure
  property_count: 6
  slug: hubspot-engagement-emails-email-engagement-structure
- name: Hubspot Engagement Emails Error Structure
  property_count: 4
  slug: hubspot-engagement-emails-error-structure
- name: Hubspot Engagement Emails Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-emails-filter-group-structure
- name: Hubspot Engagement Emails Filter Structure
  property_count: 3
  slug: hubspot-engagement-emails-filter-structure
- name: Hubspot Engagement Emails Paging Structure
  property_count: 1
  slug: hubspot-engagement-emails-paging-structure
- name: Hubspot Engagement Emails Search Request Structure
  property_count: 6
  slug: hubspot-engagement-emails-search-request-structure
- name: Hubspot Engagement Emails Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-engagement-emails-simple-public-object-input-structure
- name: Hubspot Engagement Meetings Association Structure
  property_count: 2
  slug: hubspot-engagement-meetings-association-structure
- name: Hubspot Engagement Meetings Batch Create Input Structure
  property_count: 1
  slug: hubspot-engagement-meetings-batch-create-input-structure
- name: Hubspot Engagement Meetings Batch Read Input Structure
  property_count: 2
  slug: hubspot-engagement-meetings-batch-read-input-structure
- name: Hubspot Engagement Meetings Batch Response Meeting Structure
  property_count: 3
  slug: hubspot-engagement-meetings-batch-response-meeting-structure
- name: Hubspot Engagement Meetings Batch Update Input Structure
  property_count: 1
  slug: hubspot-engagement-meetings-batch-update-input-structure
- name: Hubspot Engagement Meetings Collection Response Association Structure
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-association-structure
- name: Hubspot Engagement Meetings Collection Response Meeting Structure
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-meeting-structure
- name: Hubspot Engagement Meetings Error Structure
  property_count: 4
  slug: hubspot-engagement-meetings-error-structure
- name: Hubspot Engagement Meetings Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-meetings-filter-group-structure
- name: Hubspot Engagement Meetings Filter Structure
  property_count: 3
  slug: hubspot-engagement-meetings-filter-structure
- name: Hubspot Engagement Meetings Meeting Structure
  property_count: 6
  slug: hubspot-engagement-meetings-meeting-structure
- name: Hubspot Engagement Meetings Paging Structure
  property_count: 1
  slug: hubspot-engagement-meetings-paging-structure
- name: Hubspot Engagement Meetings Search Request Structure
  property_count: 6
  slug: hubspot-engagement-meetings-search-request-structure
- name: Hubspot Engagement Meetings Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-engagement-meetings-simple-public-object-input-structure
- name: Hubspot Engagement Notes Association Input Structure
  property_count: 2
  slug: hubspot-engagement-notes-association-input-structure
- name: Hubspot Engagement Notes Association Type Structure
  property_count: 2
  slug: hubspot-engagement-notes-association-type-structure
- name: Hubspot Engagement Notes Batch Archive Notes Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-archive-notes-request-structure
- name: Hubspot Engagement Notes Batch Create Notes Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-create-notes-request-structure
- name: Hubspot Engagement Notes Batch Error Structure
  property_count: 5
  slug: hubspot-engagement-notes-batch-error-structure
- name: Hubspot Engagement Notes Batch Notes Response Structure
  property_count: 7
  slug: hubspot-engagement-notes-batch-notes-response-structure
- name: Hubspot Engagement Notes Batch Read Input Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-read-input-structure
- name: Hubspot Engagement Notes Batch Read Notes Request Structure
  property_count: 4
  slug: hubspot-engagement-notes-batch-read-notes-request-structure
- name: Hubspot Engagement Notes Batch Update Input Structure
  property_count: 2
  slug: hubspot-engagement-notes-batch-update-input-structure
- name: Hubspot Engagement Notes Batch Update Notes Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-update-notes-request-structure
- name: Hubspot Engagement Notes Error Detail Structure
  property_count: 5
  slug: hubspot-engagement-notes-error-detail-structure
- name: Hubspot Engagement Notes Error Structure
  property_count: 7
  slug: hubspot-engagement-notes-error-structure
- name: Hubspot Engagement Notes Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-notes-filter-group-structure
- name: Hubspot Engagement Notes Filter Structure
  property_count: 5
  slug: hubspot-engagement-notes-filter-structure
- name: Hubspot Engagement Notes Gdpr Delete Request Structure
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-delete-request-structure
- name: Hubspot Engagement Notes Next Page Structure
  property_count: 2
  slug: hubspot-engagement-notes-next-page-structure
- name: Hubspot Engagement Notes Note Collection Response Structure
  property_count: 2
  slug: hubspot-engagement-notes-note-collection-response-structure
- name: Hubspot Engagement Notes Note Create Request Structure
  property_count: 2
  slug: hubspot-engagement-notes-note-create-request-structure
- name: Hubspot Engagement Notes Note Search Request Structure
  property_count: 6
  slug: hubspot-engagement-notes-note-search-request-structure
- name: Hubspot Engagement Notes Note Search Response Structure
  property_count: 3
  slug: hubspot-engagement-notes-note-search-response-structure
- name: Hubspot Engagement Notes Note Structure
  property_count: 7
  slug: hubspot-engagement-notes-note-structure
- name: Hubspot Engagement Notes Note Update Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-note-update-request-structure
- name: Hubspot Engagement Notes Paging Structure
  property_count: 1
  slug: hubspot-engagement-notes-paging-structure
- name: Hubspot Engagement Notes Property History Structure
  property_count: 6
  slug: hubspot-engagement-notes-property-history-structure
- name: Hubspot Engagement Notes Sort Option Structure
  property_count: 2
  slug: hubspot-engagement-notes-sort-option-structure
- name: Hubspot Engagement Tasks Association Structure
  property_count: 2
  slug: hubspot-engagement-tasks-association-structure
- name: Hubspot Engagement Tasks Batch Create Input Structure
  property_count: 1
  slug: hubspot-engagement-tasks-batch-create-input-structure
- name: Hubspot Engagement Tasks Batch Read Input Structure
  property_count: 2
  slug: hubspot-engagement-tasks-batch-read-input-structure
- name: Hubspot Engagement Tasks Batch Response Task Structure
  property_count: 3
  slug: hubspot-engagement-tasks-batch-response-task-structure
- name: Hubspot Engagement Tasks Batch Update Input Structure
  property_count: 1
  slug: hubspot-engagement-tasks-batch-update-input-structure
- name: Hubspot Engagement Tasks Collection Response Association Structure
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-association-structure
- name: Hubspot Engagement Tasks Collection Response Task Structure
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-task-structure
- name: Hubspot Engagement Tasks Error Structure
  property_count: 4
  slug: hubspot-engagement-tasks-error-structure
- name: Hubspot Engagement Tasks Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-tasks-filter-group-structure
- name: Hubspot Engagement Tasks Filter Structure
  property_count: 3
  slug: hubspot-engagement-tasks-filter-structure
- name: Hubspot Engagement Tasks Paging Structure
  property_count: 1
  slug: hubspot-engagement-tasks-paging-structure
- name: Hubspot Engagement Tasks Search Request Structure
  property_count: 6
  slug: hubspot-engagement-tasks-search-request-structure
- name: Hubspot Engagement Tasks Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-engagement-tasks-simple-public-object-input-structure
- name: Hubspot Engagement Tasks Task Structure
  property_count: 6
  slug: hubspot-engagement-tasks-task-structure
- name: Hubspot Marketing Emal Email Message Structure
  property_count: 6
  slug: hubspot-marketing-emal-email-message-structure
- name: Hubspot Marketing Emal Error Detail Structure
  property_count: 5
  slug: hubspot-marketing-emal-error-detail-structure
- name: Hubspot Marketing Emal Error Structure
  property_count: 7
  slug: hubspot-marketing-emal-error-structure
- name: Hubspot Marketing Emal Next Page Structure
  property_count: 2
  slug: hubspot-marketing-emal-next-page-structure
- name: Hubspot Marketing Emal Paging Structure
  property_count: 1
  slug: hubspot-marketing-emal-paging-structure
- name: Hubspot Marketing Emal Smtp Token Collection Response Structure
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-collection-response-structure
- name: Hubspot Marketing Emal Smtp Token Create Request Structure
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-create-request-structure
- name: Hubspot Marketing Emal Smtp Token Structure
  property_count: 6
  slug: hubspot-marketing-emal-smtp-token-structure
- name: Hubspot Marketing Emal Smtp Token With Password Structure
  property_count: 7
  slug: hubspot-marketing-emal-smtp-token-with-password-structure
- name: Hubspot Marketing Emal Transactional Email Request Structure
  property_count: 4
  slug: hubspot-marketing-emal-transactional-email-request-structure
- name: Hubspot Marketing Emal Transactional Email Response Structure
  property_count: 6
  slug: hubspot-marketing-emal-transactional-email-response-structure
- name: Hubspot Oauth Access Token Metadata Structure
  property_count: 9
  slug: hubspot-oauth-access-token-metadata-structure
- name: Hubspot Oauth Error Detail Structure
  property_count: 5
  slug: hubspot-oauth-error-detail-structure
- name: Hubspot Oauth Error Structure
  property_count: 7
  slug: hubspot-oauth-error-structure
- name: Hubspot Oauth Refresh Token Metadata Structure
  property_count: 6
  slug: hubspot-oauth-refresh-token-metadata-structure
- name: Hubspot Oauth Token Request Structure
  property_count: 6
  slug: hubspot-oauth-token-request-structure
- name: Hubspot Oauth Token Response Structure
  property_count: 5
  slug: hubspot-oauth-token-response-structure
- name: Hubspot Source Code Action Response Structure
  property_count: 5
  slug: hubspot-source-code-action-response-structure
- name: Hubspot Source Code Asset File Metadata Structure
  property_count: 8
  slug: hubspot-source-code-asset-file-metadata-structure
- name: Hubspot Source Code Error Detail Structure
  property_count: 5
  slug: hubspot-source-code-error-detail-structure
- name: Hubspot Source Code Error Structure
  property_count: 7
  slug: hubspot-source-code-error-structure
- name: Hubspot Source Code File Extract Request Structure
  property_count: 1
  slug: hubspot-source-code-file-extract-request-structure
- name: Hubspot Source Code File Upload Request Structure
  property_count: 1
  slug: hubspot-source-code-file-upload-request-structure
- name: Hubspot Source Code Task Locator Structure
  property_count: 2
  slug: hubspot-source-code-task-locator-structure
- name: Hubspot Source Code Validation Error Structure
  property_count: 4
  slug: hubspot-source-code-validation-error-structure
- name: Hubspot Source Code Validation Result Structure
  property_count: 3
  slug: hubspot-source-code-validation-result-structure
- name: Hubspot Source Code Validation Warning Structure
  property_count: 3
  slug: hubspot-source-code-validation-warning-structure
- name: Marketing Emal Api Email Message Structure
  property_count: 6
  slug: marketing-emal-api-email-message-structure
- name: Marketing Emal Api Next Page Structure
  property_count: 2
  slug: marketing-emal-api-next-page-structure
- name: Marketing Emal Api Paging Structure
  property_count: 1
  slug: marketing-emal-api-paging-structure
- name: Marketing Emal Api Smtp Token Collection Response Structure
  property_count: 2
  slug: marketing-emal-api-smtp-token-collection-response-structure
- name: Marketing Emal Api Smtp Token Create Request Structure
  property_count: 2
  slug: marketing-emal-api-smtp-token-create-request-structure
- name: Marketing Emal Api Smtp Token Structure
  property_count: 6
  slug: marketing-emal-api-smtp-token-structure
- name: Marketing Emal Api Smtp Token With Password Structure
  property_count: 7
  slug: marketing-emal-api-smtp-token-with-password-structure
- name: Marketing Emal Api Transactional Email Request Structure
  property_count: 4
  slug: marketing-emal-api-transactional-email-request-structure
- name: Marketing Emal Api Transactional Email Response Structure
  property_count: 6
  slug: marketing-emal-api-transactional-email-response-structure
- name: Oauth Api Access Token Metadata Structure
  property_count: 9
  slug: oauth-api-access-token-metadata-structure
- name: Oauth Api Refresh Token Metadata Structure
  property_count: 6
  slug: oauth-api-refresh-token-metadata-structure
- name: Oauth Api Token Request Structure
  property_count: 6
  slug: oauth-api-token-request-structure
- name: Oauth Api Token Response Structure
  property_count: 5
  slug: oauth-api-token-response-structure
- name: Source Code Api Action Response Structure
  property_count: 5
  slug: source-code-api-action-response-structure
- name: Source Code Api Asset File Metadata Structure
  property_count: 8
  slug: source-code-api-asset-file-metadata-structure
- name: Source Code Api File Extract Request Structure
  property_count: 1
  slug: source-code-api-file-extract-request-structure
- name: Source Code Api File Upload Request Structure
  property_count: 1
  slug: source-code-api-file-upload-request-structure
- name: Source Code Api Task Locator Structure
  property_count: 2
  slug: source-code-api-task-locator-structure
- name: Source Code Api Validation Error Structure
  property_count: 4
  slug: source-code-api-validation-error-structure
- name: Source Code Api Validation Result Structure
  property_count: 3
  slug: source-code-api-validation-result-structure
- name: Source Code Api Validation Warning Structure
  property_count: 3
  slug: source-code-api-validation-warning-structure
jsonld:
- class_count: 6
  name: Hubspot Analytics Events Api Context
  property_count: 14
  slug: hubspot-analytics-events-api-context
- class_count: 0
  name: Hubspot Analytics Events Context
  property_count: 8
  slug: hubspot-analytics-events-context
- class_count: 15
  name: Hubspot Authors Api Context
  property_count: 30
  slug: hubspot-authors-api-context
- class_count: 0
  name: Hubspot Authors Context
  property_count: 18
  slug: hubspot-authors-context
- class_count: 19
  name: Hubspot Blog Posts Api Context
  property_count: 52
  slug: hubspot-blog-posts-api-context
- class_count: 0
  name: Hubspot Blog Posts Context
  property_count: 22
  slug: hubspot-blog-posts-context
- class_count: 8
  name: Hubspot Cms Hubdb Api Context
  property_count: 15
  slug: hubspot-cms-hubdb-api-context
- class_count: 0
  name: Hubspot Cms Hubdb Context
  property_count: 9
  slug: hubspot-cms-hubdb-context
- class_count: 5
  name: Hubspot Cms Pages Api Context
  property_count: 20
  slug: hubspot-cms-pages-api-context
- class_count: 0
  name: Hubspot Cms Pages Context
  property_count: 6
  slug: hubspot-cms-pages-context
- class_count: 24
  name: Hubspot Commerce Payments Api Context
  property_count: 47
  slug: hubspot-commerce-payments-api-context
- class_count: 0
  name: Hubspot Commerce Payments Context
  property_count: 26
  slug: hubspot-commerce-payments-context
- class_count: 13
  name: Hubspot Commerce Subscriptions Api Context
  property_count: 22
  slug: hubspot-commerce-subscriptions-api-context
- class_count: 0
  name: Hubspot Commerce Subscriptions Context
  property_count: 14
  slug: hubspot-commerce-subscriptions-context
- class_count: 1
  name: Hubspot Context
  property_count: 49
  slug: hubspot-context
- class_count: 17
  name: Hubspot Conversations Api Context
  property_count: 40
  slug: hubspot-conversations-api-context
- class_count: 0
  name: Hubspot Conversations Context
  property_count: 19
  slug: hubspot-conversations-context
- class_count: 19
  name: Hubspot Crm Associations Api Context
  property_count: 28
  slug: hubspot-crm-associations-api-context
- class_count: 0
  name: Hubspot Crm Associations Context
  property_count: 22
  slug: hubspot-crm-associations-context
- class_count: 14
  name: Hubspot Crm Companies Api Context
  property_count: 22
  slug: hubspot-crm-companies-api-context
- class_count: 0
  name: Hubspot Crm Companies Context
  property_count: 15
  slug: hubspot-crm-companies-context
- class_count: 14
  name: Hubspot Crm Contacts Api Context
  property_count: 22
  slug: hubspot-crm-contacts-api-context
- class_count: 0
  name: Hubspot Crm Contacts Context
  property_count: 15
  slug: hubspot-crm-contacts-context
- class_count: 14
  name: Hubspot Crm Deals Api Context
  property_count: 22
  slug: hubspot-crm-deals-api-context
- class_count: 0
  name: Hubspot Crm Deals Context
  property_count: 15
  slug: hubspot-crm-deals-context
- class_count: 14
  name: Hubspot Crm Feature Flags Api Context
  property_count: 20
  slug: hubspot-crm-feature-flags-api-context
- class_count: 0
  name: Hubspot Crm Feature Flags Context
  property_count: 16
  slug: hubspot-crm-feature-flags-context
- class_count: 8
  name: Hubspot Crm Lists Api Context
  property_count: 21
  slug: hubspot-crm-lists-api-context
- class_count: 0
  name: Hubspot Crm Lists Context
  property_count: 9
  slug: hubspot-crm-lists-context
- class_count: 7
  name: Hubspot Crm Search Api Context
  property_count: 21
  slug: hubspot-crm-search-api-context
- class_count: 0
  name: Hubspot Crm Search Context
  property_count: 8
  slug: hubspot-crm-search-context
- class_count: 14
  name: Hubspot Crm Tickets Api Context
  property_count: 22
  slug: hubspot-crm-tickets-api-context
- class_count: 0
  name: Hubspot Crm Tickets Context
  property_count: 15
  slug: hubspot-crm-tickets-context
- class_count: 22
  name: Hubspot Custom Workflow Actions Api Context
  property_count: 39
  slug: hubspot-custom-workflow-actions-api-context
- class_count: 0
  name: Hubspot Custom Workflow Actions Context
  property_count: 24
  slug: hubspot-custom-workflow-actions-context
- class_count: 4
  name: Hubspot Domains Api Context
  property_count: 27
  slug: hubspot-domains-api-context
- class_count: 0
  name: Hubspot Domains Context
  property_count: 6
  slug: hubspot-domains-context
- class_count: 23
  name: Hubspot Engagement Calls Api Context
  property_count: 46
  slug: hubspot-engagement-calls-api-context
- class_count: 0
  name: Hubspot Engagement Calls Context
  property_count: 25
  slug: hubspot-engagement-calls-context
- class_count: 13
  name: Hubspot Engagement Emails Api Context
  property_count: 22
  slug: hubspot-engagement-emails-api-context
- class_count: 0
  name: Hubspot Engagement Emails Context
  property_count: 14
  slug: hubspot-engagement-emails-context
- class_count: 13
  name: Hubspot Engagement Meetings Api Context
  property_count: 22
  slug: hubspot-engagement-meetings-api-context
- class_count: 0
  name: Hubspot Engagement Meetings Context
  property_count: 14
  slug: hubspot-engagement-meetings-context
- class_count: 2
  name: Hubspot Engagement Notes Association Context
  property_count: 4
  slug: hubspot-engagement-notes-association-context
- class_count: 8
  name: Hubspot Engagement Notes Batch Context
  property_count: 15
  slug: hubspot-engagement-notes-batch-context
- class_count: 0
  name: Hubspot Engagement Notes Context
  property_count: 25
  slug: hubspot-engagement-notes-context
- class_count: 2
  name: Hubspot Engagement Notes Filter Context
  property_count: 6
  slug: hubspot-engagement-notes-filter-context
- class_count: 1
  name: Hubspot Engagement Notes Gdpr Context
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-context
- class_count: 1
  name: Hubspot Engagement Notes Next Context
  property_count: 2
  slug: hubspot-engagement-notes-next-context
- class_count: 6
  name: Hubspot Engagement Notes Note Context
  property_count: 16
  slug: hubspot-engagement-notes-note-context
- class_count: 1
  name: Hubspot Engagement Notes Paging Context
  property_count: 1
  slug: hubspot-engagement-notes-paging-context
- class_count: 1
  name: Hubspot Engagement Notes Property Context
  property_count: 6
  slug: hubspot-engagement-notes-property-context
- class_count: 1
  name: Hubspot Engagement Notes Sort Context
  property_count: 2
  slug: hubspot-engagement-notes-sort-context
- class_count: 13
  name: Hubspot Engagement Tasks Api Context
  property_count: 22
  slug: hubspot-engagement-tasks-api-context
- class_count: 0
  name: Hubspot Engagement Tasks Context
  property_count: 14
  slug: hubspot-engagement-tasks-context
- class_count: 9
  name: Hubspot Marketing Emal Api Context
  property_count: 28
  slug: hubspot-marketing-emal-api-context
- class_count: 0
  name: Hubspot Marketing Emal Context
  property_count: 11
  slug: hubspot-marketing-emal-context
- class_count: 4
  name: Hubspot Oauth Api Context
  property_count: 17
  slug: hubspot-oauth-api-context
- class_count: 0
  name: Hubspot Oauth Context
  property_count: 6
  slug: hubspot-oauth-context
- class_count: 8
  name: Hubspot Source Code Api Context
  property_count: 23
  slug: hubspot-source-code-api-context
- class_count: 0
  name: Hubspot Source Code Context
  property_count: 10
  slug: hubspot-source-code-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-08-13'
name: HubSpot
nav: Providers
network: true
overview: 'HubSpot publishes 57 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Webhooks API, Access Tokens API, and 54 more. Tagged areas include Analytics, Commerce, Content, CRM, and Customer Service.


  The HubSpot catalog on APIs.io includes 1 event-driven AsyncAPI specification, 61 JSON-LD contexts, and 3 Spectral governance rulesets.


  HubSpot''s developer surface includes authentication, API reference, developer portal, documentation, changelog, support, engineering blog, and 138 more developer resources.'
plans:
- name: Hubspot Plans Pricing
  plan_count: 4
  slug: hubspot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Hubspot Rate Limits
  slug: hubspot-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: HubSpot API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: hubspot-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: HubSpot API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hubspot-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: HubSpot API Rules
  rule_count: 28
  severity_counts:
    error: 19
    hint: 0
    info: 2
    warn: 7
  slug: hubspot-spectral-rules
scopes:
- name: Hubspot Scopes
  scope_count: 29
  slug: hubspot-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: exemplar
  composite: 80.2
  coverage:
    artifact_dirs: 40
    catalog_gap: 34.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 82.4
    developer_ergonomics: 94.6
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 71.1
  previous_composite: 80.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/screenshots/hubspot-2026-06-20T182920.png
security:
- kind: authentication
  name: Hubspot Authentication
  slug: hubspot-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Hubspot Domain Security
  slug: hubspot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hubspot Vulnerability Disclosure
  slug: hubspot-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hubspot Trust Center
  slug: hubspot-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: hubspot
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Sales
use_cases:
- description: Use AI to generate blog posts, social media content, and marketing copy at scale.
  name: AI-Powered Content Creation
- description: Leverage AI for lead scoring, deal forecasting, and automated sales email generation.
  name: AI-Powered Sales
- description: Track and analyze marketing, sales, and service performance with unified reporting dashboards.
  name: Analytics
- description: Create, manage, and publish website content, blog posts, and landing pages.
  name: Content Creation and Management
- description: Centralized content management for creating and distributing content across channels.
  name: Content Hub
- description: Manage customer support tickets, knowledge base, and feedback surveys.
  name: Customer Service
- description: Automate ticket routing, responses, and escalation with workflow-based support.
  name: Customer Support Automation
- description: Clean, deduplicate, and enrich CRM data with automated data quality tools.
  name: Data Management and Insights
- description: Track deals through customizable pipeline stages with forecasting and reporting.
  name: Deal Management
- description: Design, send, and analyze marketing email campaigns with segmentation and A/B testing.
  name: Email Marketing
- description: Connect with 1,500+ integrations in the HubSpot App Marketplace.
  name: HubSpot Ecosystem
- description: Attract visitors with SEO, blogs, and social media, then convert them with forms and CTAs.
  name: Inbound Marketing
- description: Connect apps and automate business processes with programmable workflows.
  name: Integration and Automation
- description: Build landing pages with embedded forms to capture and qualify leads.
  name: Landing Pages & Forms
- description: Capture leads through forms, chatbots, and CTAs, then nurture with automated sequences.
  name: Lead Generation and Conversion
- description: Engage website visitors in real-time with live chat and route conversations to the right team.
  name: Live Chat
- description: Sync, clean, and automate business data across systems with programmable automation.
  name: Operations Hub
- description: Manage sales teams with activity tracking, quotas, forecasting, and coaching tools.
  name: Sales Management
- description: Deliver customer service with ticketing, knowledge base, feedback, and customer portal.
  name: Service Hub
- description: Automate repetitive tasks across marketing, sales, and service with visual workflow builder.
  name: Workflows
website: https://developers.hubspot.com/
---
